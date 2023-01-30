import asyncio
import json
#from aiokafka import AIOKafkaConsumer
from pydantic import BaseModel, StrictStr
#from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from fastapi import FastAPI

app = FastAPI()


#aioproducer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_INSTANCE)
class Producer(BaseModel):
    id: int
    topic: str
    message: str
   
    
# POST for producer registration
@app.post("/{producer_id}/{topic}/register")
def producer_registration(producer_id: int, topic):
    return {'Data':{'producer_id':producer_id,
                    'topic':topic}}

@app.post("/{topic}/{producer_id}/{message}/enqueue")
def producer_enqueue(topic, producer_id: int, message):
    return {'Data':{'topic':topic,'producer_id':producer_id,'message':message}}