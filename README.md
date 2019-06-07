# NATS-Demo
Demo for NATS message queue PUB/SUB pattern
1.   
#Run on local  
pip install asyncio  
pip install asyncio-nats-client  
#Run 1 subcriber
python sub.py  
#Run 1000 subcribers 
python stress_test.py 1000 1000  
#Publish a message
python pub.py  

2.  
#Deploy on docker-compose  
cd flask-nats  
docker-compose up --build  
#open new shell and
#Run 1 subcriber
python sub.py  
#Run 1000 subcribers 
python stress_test.py 1000 1000  
#publish a message by access http://localhost:5000/send  
And see message in log  

3. Deploy NATS cluster  
cd flask-nats-cluster  
docker-compose up --build  
#publish a message by access http://localhost:5000/send  

use sub.py and stress_test.py for test message



