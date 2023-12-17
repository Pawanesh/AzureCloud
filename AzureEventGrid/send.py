import datetime
import uuid


from azure.core.credentials import AzureKeyCredential
from azure.eventgrid import EventGridPublisherClient, EventGridEvent

# If you wish to debug
# import logging
# logging.basicConfig(level=logging.DEBUG)

# Enter values for <topic-name> and <region>
TOPIC_ENDPOINT = "https://event-grid-topic-pg230.eastus-1.eventgrid.azure.net/api/events"

# Enter value for <topic-key>
EVENT_GRID_KEY = '/BfCtSvfhPE6+oIXUTYGlr4Q/j7YLirv0zCSdHU+W78='


def build_events_list():
    # type: () -> List[EventGridEvent]
    result = []
    for i in range(5):
        result.append(EventGridEvent(
            id=uuid.uuid4(),
            subject="My subject {}".format(i),
            data={
                'key': 'I accept any kind of data here, this is a free dictionary'
            },
            event_type='PersonalEventType',
            event_time=datetime.datetime.now(),
            data_version=2.0
        ))
    return result


def run_example():

    credentials = AzureKeyCredential(
        EVENT_GRID_KEY
    )
    event_grid_client = EventGridPublisherClient(TOPIC_ENDPOINT, credentials)
    events=build_events_list()

    event_grid_client.send(events)

    print("Published events to Event Grid.")


if __name__ == "__main__":
    run_example()
()