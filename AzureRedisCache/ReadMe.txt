#Login to azure account 
    az login

#Create resource group
    az group create --resource-group redis-rg --location eastus

#Create redis cache instanceView
    az redis create --name redis-cache-pg230 --resource-group redis-rg --location eastus --sku basic --vm-size C0


#Redis show
    az redis show --name redis-cache-pg230 --resource-group redis-rg -o table
    EnableNonSslPort    HostName                                   Location    Name               Port    ProvisioningState    PublicNetworkAccess    RedisVersion    ResourceGroup    SslPort
    ------------------  -----------------------------------------  ----------  -----------------  ------  -------------------  ---------------------  --------------  ---------------  ---------
    False               redis-cache-pg230.redis.cache.windows.net  East US     redis-cache-pg230  6379    Succeeded            Enabled                6.0             redis-rg         6380


#Redis key show
    az redis list-keys --name redis-cache-pg230 --resource-group redis-rg -o table                                        
    PrimaryKey                                    SecondaryKey
    --------------------------------------------  --------------------------------------------
    vNjopGZKGgsXqQl3xAQoN9mFikBliAjozAzCaKGxXCo=  FWhqFiKjX5bCkxUk74UsD0UG1Tcrhm50AAzCaPvYwls=


python -m venv .venv

source .venv/bin/activate

pip install redis   

export REDIS_HOSTNAME=redis-cache-pg230.redis.cache.windows.net
export REDIS_KEY=vNjopGZKGgsXqQl3xAQoN9mFikBliAjozAzCaKGxXCo=
export REDIS_PORT=6380

python app.py 
    Ping returned : True
    SET Message returned : True
    GET Message returned : Hello!, The cache is working with Python!
    CLIENT LIST returned : 
    id : 7628, addr : 74.14.54.143:63675
