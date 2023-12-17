#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import os
import asyncio
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
from azure.identity.aio import DefaultAzureCredential
from azure.schemaregistry.aio import SchemaRegistryClient
from azure.schemaregistry.encoder.avroencoder.aio import AvroEncoder

EVENT_HUB_FULLY_QUALIFIED_NAMESPACE = "event-hub-ns-pg230.servicebus.windows.net"
EVENT_HUB_NAME = "event-hub-pg230"



SCHEMAREGISTRY_FULLY_QUALIFIED_NAMESPACE = "event-hub-ns-pg230.servicebus.windows.net"
GROUP_NAME = "event-schema-group"

SCHEMA_STRING = """
{"namespace": "example.avro",
 "type": "record",
 "name": "User",
 "fields": [
     {"name": "name", "type": "string"},
     {"name": "favorite_number",  "type": ["int", "null"]},
     {"name": "favorite_color", "type": ["string", "null"]}
 ]
}"""


# create a AvroEncoder instance
azure_credential = DefaultAzureCredential()

eventhub_producer = EventHubProducerClient(
    fully_qualified_namespace=EVENT_HUB_FULLY_QUALIFIED_NAMESPACE,
    eventhub_name=EVENT_HUB_NAME,
    credential=azure_credential,
)

# create a AvroEncoder instance
avro_encoder = AvroEncoder(
    client=SchemaRegistryClient(
        fully_qualified_namespace=SCHEMAREGISTRY_FULLY_QUALIFIED_NAMESPACE,
        credential=azure_credential
    ),
    group_name=GROUP_NAME,
    auto_register=True
)

async def send_event_data_batch(producer, encoder):
    event_data_batch = await producer.create_batch()
    dict_content_1 = {"name": "Bob", "favorite_number": 7, "favorite_color": "red"}
    # Use the encode method to convert dict object to bytes with the given avro schema and set body of EventData.
    # The encode method will automatically register the schema into the Schema Registry Service and
    # schema will be cached locally for future usage.
    event_data_1 = await encoder.encode(content=dict_content_1, schema=SCHEMA_STRING, message_type=EventData)
    print(f'The bytes of encoded dict content is {next(event_data_1.body)}.')

    event_data_batch.add(event_data_1)


    dict_content_2 = {"name": "Pawanesh", "favorite_number": 29, "favorite_color": "Blue"}
    # Use the encode method to convert dict object to bytes with the given avro schema and set body of EventData.
    # The encode method will automatically register the schema into the Schema Registry Service and
    # schema will be cached locally for future usage.
    event_data_2 = await encoder.encode(content=dict_content_2, schema=SCHEMA_STRING, message_type=EventData)
    print(f'The bytes of encoded dict content is {next(event_data_2.body)}.')

    event_data_batch.add(event_data_2)


    await producer.send_batch(event_data_batch)
    print('Send is done.')


async def main():

    await send_event_data_batch(eventhub_producer, avro_encoder)
    await avro_encoder.close()
    await azure_credential.close()
    await eventhub_producer.close()

if __name__ == "__main__":
    asyncio.run(main())