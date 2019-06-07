import asyncio
from nats.aio.client import Client as NATS
import redis
r = redis.Redis(host='192.168.1.200', port=6379, db=0)

async def example():

   # [begin subscribe_async]
   nc = NATS()

   await nc.connect(servers=["nats://178.128.212.211:4222", "nats://188.166.238.142:4222", "nats://139.59.245.168:4222"])

   future = asyncio.Future()

   async def cb(msg):
     nonlocal future
     future.set_result(msg)

   await nc.subscribe("msg", cb=cb)
   # await nc.publish("msg", b'All is Well')
   await nc.flush()

   # Wait for message to come in
   msg = await asyncio.wait_for(future, 100000000000000000)

   # [end subscribe_async]
   print(msg)
   print(r.incr("key1"))

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
