import redis
import os

myHostname = os.environ['REDIS_HOSTNAME']
myPassword = os.environ['REDIS_KEY']
myPort = os.environ['REDIS_PORT']
r = redis.StrictRedis(host=myHostname, port=myPort,
                      password=myPassword, ssl=True)

result = r.ping()
print("Ping returned : " + str(result))

result = r.set("Message", "Hello!, The cache is working with Python!")
print("SET Message returned : " + str(result))

result = r.get("Message")
print("GET Message returned : " + result.decode("utf-8"))

result = r.client_list()
print("CLIENT LIST returned : ")
for c in result:
    print(f"id : {c['id']}, addr : {c['addr']}")