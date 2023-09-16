Create resource group
    az group create --name event-hub-rg --location eastus

Create an Event Hubs namespace
    az eventhubs namespace create --name event-hub-ns-pg230 --resource-group event-hub-rg --location eastus

Create an Event Hub
    az eventhubs eventhub create --name event-hub-pg230 --resource-group event-hub-rg  --namespace-name event-hub-ns-pg230

Get namespaceid
    az eventhubs  namespace show -g event-hub-rg -n event-hub-ns-pg230   --query id
    "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourceGroups/event-hub-rg/providers/Microsoft.EventHub/namespaces/event-hub-ns-pg230"

Add assigned role
    az role assignment create --assignee "pawgupta0@publicisgroupe.net" \
    --role "Azure Event Hubs Data Owner" \
    --scope "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourceGroups/event-hub-rg/providers/Microsoft.EventHub/namespaces/event-hub-ns-pg230"

Python venv
    python -m venv .venv
    source .venv/bin/activate

    pip install azure-eventhub
    pip install azure-identity
    pip install aiohttp
    pip install azure-identity

Create blob storage 
    az storage account create --name eventhubstoragepg230 --resource-group event-hub-rg --sku Standard_LRS --location eastus

    az storage container create --name event-hub-checkpoint --account-name eventhubstoragepg230


Add assigned role to storage account
    az storage account show --resource-group event-hub-rg --name eventhubstoragepg230 --query id
    "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourceGroups/event-hub-rg/providers/Microsoft.Storage/storageAccounts/eventhubstoragepg230"

    az role assignment create --assignee "pawgupta0@publicisgroupe.net" \
    --role "Storage Blob Data Contributor" \
    --scope "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourceGroups/event-hub-rg/providers/Microsoft.Storage/storageAccounts/eventhubstoragepg230"

Run producer
    python send.py

Run consumer
    AzureEventHub % python recv.py
    Received the event: "First event " from the partition with ID: "3"
    Received the event: "Second event" from the partition with ID: "3"
    Received the event: "First event " from the partition with ID: "1"
    Received the event: "First event " from the partition with ID: "2"
    Received the event: "Third event" from the partition with ID: "3"

