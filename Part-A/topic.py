from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
# from fastapi import APIRouter

# router = APIRouter()
app = FastAPI()

topics = ['topic1', 'topic2']
@app.get("/topics")
def get_topics():
    
    return {"topics": topics}

class Topic(BaseModel):
    name: str
    
@app.post("/topics/{topic}")
def create_topic(topic):
    if topic in topics:
        raise HTTPException(status_code=409,detail="topic is already in topic list")
    return {"Topic":topic}
