import os
import json
from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential

endpoint = os.environ["COSMOS_ENDPOINT"]


DATABASE_NAME = "cosmicworks"
CONTAINER_NAME = "products"


credential = DefaultAzureCredential()
client = CosmosClient(url=endpoint, credential=credential)

dbproxy = client.get_database_client(DATABASE_NAME)

containerProxy = dbproxy.get_container_client(CONTAINER_NAME)

new_item = {
    "id": "1",
    "categoryId": "1",
    "categoryName": "gear-surf-surfboards",
    "name": "Yamba Surfboard",
    "quantity": 12,
    "sale": False,
}


containerProxy.create_item(new_item)

QUERY = "SELECT * FROM products p WHERE p.categoryId = @categoryId"
CATEGORYID = "1"
params = [dict(name="@categoryId", value=CATEGORYID)]

results = containerProxy.query_items(
    query=QUERY, parameters=params, enable_cross_partition_query=False
)

items = [item for item in results]
output = json.dumps(items, indent=True)
print("Result list\t", output)