https://microsoftlearning.github.io/AZ-204-DevelopingSolutionsforMicrosoftAzure/Instructions/Labs/AZ-204_lab_09.html

Create resource group
    az group create --name event-grid-rg --location eastus

python venv
    python -m venv .venv
    source .venv/bin/activate
    pip install azure-eventgrid 


Create a custom Event Grid topic
    az eventgrid topic create --name event-grid-topic-pg230 --resource-group event-grid-rg --location eastus --input-schema eventgridschema



Deploy the Azure Event Grid viewer to a web app

    az appservice plan create -g event-grid-rg  -n event-grid-web-app-plan --is-linux --number-of-workers 1 --sku B1


    az webapp create -g event-grid-rg  -p event-grid-web-app-plan -n event-grid-web-app -i microsoftlearning/azure-event-grid-viewer:latest --runtime "python:3.9"


Exercise 2: Create an Event Grid subscription
    Webapp default domain:  event-grid-web-app-pg230.azurewebsites.net


Task 4: Record subscription credentials
    Topic end point: https://event-grid-topic-pg230.eastus-1.eventgrid.azure.net/api/events

    Key1: /BfCtSvfhPE6+oIXUTYGlr4Q/j7YLirv0zCSdHU+W78=


Run publisher
    pyhton send.py
    Verify the the events on eventviewer https://event-grid-web-app-pg230.azurewebsites.net


