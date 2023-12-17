#Create resource group
    az group create --name key-vault-rg --location eastus

#Create keyvalut
    az keyvault create --name keyvault-pawgupta0 -g key-vault-rg -l eastus

#Set secret and value
    az keyvault secret set --name secret-password --value Password@123 --vault-name keyvault-pawgupta0
    {
    "attributes": {
        "created": "2023-10-18T20:31:24+00:00",
        "enabled": true,
        "expires": null,
        "notBefore": null,
        "recoverableDays": 90,
        "recoveryLevel": "Recoverable+Purgeable",
        "updated": "2023-10-18T20:31:24+00:00"
    },
    "contentType": null,
    "id": "https://keyvault-pawgupta0.vault.azure.net/secrets/secret-password/319e2cd2e6444b96b8a0110c303414d1",
    "kid": null,
    "managed": null,
    "name": "secret-password",
    "tags": {
        "file-encoding": "utf-8"
    },
    "value": "Password@123"
    }
    
#Show secrets
    az keyvault secret show --name secret-password --vault-name keyvault-pawgupta0 -o table
    Name             Value
    ---------------  ------------
    secret-password  Password@123

#Create a new user-assigned managed identity with a name of your choice:
    az identity create --name identity-app-pawgupta0 -g key-vault-rg
