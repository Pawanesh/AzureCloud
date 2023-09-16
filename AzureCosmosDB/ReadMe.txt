# Create an Azure Cosmos DB account


#This quickstart will create a single Azure Cosmos DB account using the API for NoSQL.


# Variable for resource group name
resourceGroupName="cosmos-db-quickstart-rg"
location="eastus"

accountName="cosmos-db-quickstart-acc"



az group create --name $resourceGroupName --location $location


az cosmosdb create --resource-group $resourceGroupName --name $accountName --locations regionName=$location --enable-free-tier true


az cosmosdb show --resource-group $resourceGroupName --name $accountName --query "documentEndpoint"

    "https://cosmos-db-quickstart-acc.documents.azure.com:443/"


az cosmosdb keys list --resource-group $resourceGroupName --name $accountName --type "keys" --query "primaryMasterKey"

    "Jc8wgyyd7OQQoJvRAcLRFwrz9hA58pZHJpq0vvtZFFCowfJjCDcOmLNILcBIPbb1SjKuvSCPZqyXACDbCaKM7w=="


python -m venv .venv 

source .venv/bin/activate

pip install azure-cosmos

pip install azure-identity


export COSMOS_ENDPOINT="https://cosmos-db-quickstart-acc.documents.azure.com:443/"
export COSMOS_KEY="Jc8wgyyd7OQQoJvRAcLRFwrz9hA58pZHJpq0vvtZFFCowfJjCDcOmLNILcBIPbb1SjKuvSCPZqyXACDbCaKM7w=="


#Create the custom role

az cosmosdb sql role definition create \
    --account-name cosmos-db-quickstart-acc \
    --resource-group  cosmos-db-quickstart-rg \
    --body '{
    "RoleName": "PasswordlessReadWrite",
    "Type": "CustomRole",
    "AssignableScopes": ["/"],
    "Permissions": [{
        "DataActions": [
            "Microsoft.DocumentDB/databaseAccounts/readMetadata",
            "Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/items/*",
            "Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/*"
        ]
    }]
}'

                {
                "assignableScopes": [
                    "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourceGroups/cosmos-db-quickstart-rg/providers/Microsoft.DocumentDB/databaseAccounts/cosmos-db-quickstart-acc"
                ],
                "id": "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourceGroups/cosmos-db-quickstart-rg/providers/Microsoft.DocumentDB/databaseAccounts/cosmos-db-quickstart-acc/sqlRoleDefinitions/67b5c9dc-26d7-400b-b040-0a828e7284a7",
                "name": "67b5c9dc-26d7-400b-b040-0a828e7284a7",
                "permissions": [
                    {
                    "dataActions": [
                        "Microsoft.DocumentDB/databaseAccounts/readMetadata",
                        "Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/items/*",
                        "Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/*"
                    ],
                    "notDataActions": []
                    }
                ],
                "resourceGroup": "cosmos-db-quickstart-rg",
                "roleName": "PasswordlessReadWrite",
                "type": "Microsoft.DocumentDB/databaseAccounts/sqlRoleDefinitions",
                "typePropertiesType": "CustomRole"
                }


az ad user show --id "pawgupta0@publicisgroupe.net"     
            {
            "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity",
            "businessPhones": [
                "+13126965110"
            ],
            "displayName": "Pawanesh Gupta",
            "givenName": "Pawanesh",
            "id": "602ce796-dbde-458e-bd8b-79ad22587734",
            "jobTitle": "Specialist Platform",
            "mail": "pawanesh.gupta@publicissapient.com",
            "mobilePhone": "+13122926187",
            "officeLocation": "CA ON Toronto 134 Peter Street",
            "preferredLanguage": null,
            "surname": "Gupta",
            "userPrincipalName": "pawgupta0@publicisgroupe.net"



az cosmosdb sql role assignment create \
    --account-name cosmos-db-quickstart-acc \
    --resource-group  cosmos-db-quickstart-rg \
    --scope "/" \
    --principal-id 602ce796-dbde-458e-bd8b-79ad22587734 \
    --role-definition-id 67b5c9dc-26d7-400b-b040-0a828e7284a7



# Create a SQL API database 
az cosmosdb sql database create --account-name cosmos-db-quickstart-acc --resource-group cosmos-db-quickstart-rg --name cosmicworks



# Create a SQL API container
az cosmosdb sql container create \
    --account-name cosmos-db-quickstart-acc \
    --resource-group cosmos-db-quickstart-rg \
    --database-name cosmicworks \
    --partition-key-path "/categoryId" \
    --name products



#Run app
python app.py