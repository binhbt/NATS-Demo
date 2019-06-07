import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin publish_bytes]
   nc = NATS()

   await nc.connect(servers=["nats://nats:4222"])

   await nc.publish("msg", b'All is Well')

   # [end publish_bytes]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()