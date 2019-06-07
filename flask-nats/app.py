from flask import Flask
from redis import Redis
import asyncio
from nats.aio.client import Client as NATS


# async def example():

#     # [begin publish_bytes]
#     nc = NATS()

#     await nc.connect(servers=["nats://192.168.1.32:4222"])

#     await nc.publish("msg", b'All is Well')

#     # [end publish_bytes]

#     await nc.close()

import subprocess
def excute_command(command):
   print(command)
   subprocess.run(command, shell=True)

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
app.config["REDIS_URL"] = "redis://redis:6379"


@app.route('/')
def hello():

    return 'Hello World! I have been seen %s times.' % redis.get('counter')


@app.route('/send')
def send_message():
    redis.incr('counter')
    excute_command('python pub.py')
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(example())
    # loop.close()
    return "Message sent!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
