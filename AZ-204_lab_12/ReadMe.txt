Lab 12: Enhance a web application by using the Azure Content Delivery Network
https://microsoftlearning.github.io/AZ-204-DevelopingSolutionsforMicrosoftAzure/Instructions/Labs/AZ-204_lab_12.html



#Create resource group cdn-rg 
    az group create --name cdn-rg --location eastus

#Create storage account cdnstoragepg230
    az storage account create --name cdnstoragepg230 --resource-group cdn-rg --location eastus --sku Standard_LRS --tags createdby=Pawanesh env=dev  

#Create blob container in storate account

Media blob url: https://cdnstoragepg230.blob.core.windows.net/media
Video blob url: https://cdnstoragepg230.blob.core.windows.net/video

CDN Media end point: https://cdn-media.azureedge.net
CDN Video end point: https://cdn-video.azureedge.net
CDN Webapp end Point: https://cdn-web-app.azureedge.net