https://learn.microsoft.com/en-us/training/modules/explore-api-management/8-exercise-import-api



#Create a resource group. The following commands create a resource group named apim-rg
#Create group
az group create --name apim-rg --location eastus

#Create api management instance
az apim create --name apim-pg230 --resource-group apim-rg --location eastus --publisher-name apim-publisher --publisher-email pawgupta0@publicisgroupe.net  --sku-name Consumption