from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
# from fastapi import APIRouter

# router = APIRouter()

app = FastAPI()

class Producer(BaseModel):
    id: int
    topic: str

topics = []

# POST for registering user
@app.post('/{producer_id}/{topic_id}/register')
def register_consumer(producer_id: int, topic_id: int):
    if topic_id not in topics:
        # raise HTTPException(status_code=404, detail="Topic not found")
        pass
    return {'Data':{'ProducerId':producer_id,
                    'Topic':topic_id}}


# GET for dequeue
@app.post('/{producer_id}/{topic_id}/{message}/produce')
def dequeue_topic(consumer_id: int, topic_id: int, message: str):
    if topic_id not in topics:
        raise HTTPException(status_code=404, detail="Not subscribed")
    return {'Data':{'ProducerId':consumer_id,
                    'Topic':topic_id,
                    'Message': message}}
