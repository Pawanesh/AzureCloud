#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.identity.aio import DefaultAzureCredential
from azure.schemaregistry.aio import SchemaRegistryClient
from azure.schemaregistry.encoder.avroencoder.aio import AvroEncoder
from azure.eventhub.extensions.checkpointstoreblobaio import (
    BlobCheckpointStore,
)

EVENT_HUB_FULLY_QUALIFIED_NAMESPACE = "event-hub-ns-pg230.servicebus.windows.net"
EVENT_HUB_NAME = "event-hub-pg230"



SCHEMAREGISTRY_FULLY_QUALIFIED_NAMESPACE = "event-hub-ns-pg230.servicebus.windows.net"
GROUP_NAME = "event-schema-group"

BLOB_STORAGE_ACCOUNT_URL = "https://eventhubstoragepg230.blob.core.windows.net/"
BLOB_CONTAINER_NAME = "event-hub-checkpoint"


# create a AvroEncoder instance
azure_credential = DefaultAzureCredential()


checkpoint_store = BlobCheckpointStore(
    blob_account_url=BLOB_STORAGE_ACCOUNT_URL,
    container_name=BLOB_CONTAINER_NAME,
    credential=azure_credential,
)

# Create a consumer client for the event hub.
eventhub_consumer = EventHubConsumerClient(
    fully_qualified_namespace=EVENT_HUB_FULLY_QUALIFIED_NAMESPACE,
    eventhub_name=EVENT_HUB_NAME,
    consumer_group="$Default",
    checkpoint_store=checkpoint_store,
    credential=azure_credential,
    )



avro_encoder = AvroEncoder(
    client=SchemaRegistryClient(
        fully_qualified_namespace=SCHEMAREGISTRY_FULLY_QUALIFIED_NAMESPACE,
        credential=azure_credential
    ),
    group_name=GROUP_NAME,
    auto_register=True
)

async def on_event(partition_context, event):
    print(f"Received event from partition: {partition_context.partition_id}.")

    bytes_payload = b"".join(b for b in event.body)
    print(f'The received bytes of the EventData is {bytes_payload!r}.')

    # Use the decode method to decode the payload of the event.
    # The decode method will extract the schema id from the content_type, and automatically retrieve the Avro Schema
    # from the Schema Registry Service. The schema will be cached locally for future usage.
    decoded_content= await avro_encoder.decode(event)
    print(f'The dict content after decoding is {decoded_content}')


async def main():
    try:
        async with eventhub_consumer, avro_encoder:
            await eventhub_consumer.receive(
                on_event=on_event,
                starting_position="-1",  # "-1" is from the beginning of the partition.
            )
    except KeyboardInterrupt:
        print('Stopped receiving.')
    finally:
        await avro_encoder.close()
        await azure_credential.close()
        await eventhub_consumer.close()

if __name__ == '__main__':
    asyncio.run(main())