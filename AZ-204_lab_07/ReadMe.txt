https://microsoftlearning.github.io/AZ-204-DevelopingSolutionsforMicrosoftAzure/Instructions/Labs/AZ-204_lab_07.html#lab-scenario


Resource Group:
    Name: ConfidentialStack-RG

Storage Account
    Name: confidentialstorageacc


Storage Account Connection string
    DefaultEndpointsProtocol=https;AccountName=confidentialstorageacc;AccountKey=NsZ6Gfohu5ssmwSvWBIKFC8fKGoLvz1hbWQeCLYnLTpg1YMIKC5afzt3qtTUIQxfF2kSgsTwjIz7+AStWAoh4Q==;EndpointSuffix=core.windows.net


KeyVault 
    Name: securekeyvault-KV



Function App
    Name: securefunctionapp

Keyvault secret 
    Name: storagecredentials
    Secret Identifier: https://securekeyvault-kv.vault.azure.net/secrets/storagecredentials/1eba33b24e6f474c8ccba413ccf7b9d0
    Secret Value: DefaultEndpointsProtocol=https;AccountName=confidentialstorageacc;AccountKey=NsZ6Gfohu5ssmwSvWBIKFC8fKGoLvz1hbWQeCLYnLTpg1YMIKC5afzt3qtTUIQxfF2kSgsTwjIz7+AStWAoh4Q==;EndpointSuffix=core.windows.net


FunctionAppCreate a Key Vault-derived application setting
    StorageConnectionString 
    @Microsoft.KeyVault(SecretUri=<Secret Identifier>)

    @Microsoft.KeyVault(SecretUri=https://securekeyvault-kv.vault.azure.net/secrets/storagecredentials/1eba33b24e6f474c8ccba413ccf7b9d0)


Deploy function in function app
    func azure functionapp publish securefunctionapp