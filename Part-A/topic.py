from fastapi import FastAPI
from pydantic import BaseModel
# from fastapi import APIRouter

# router = APIRouter()
app = FastAPI()


@app.get("/topics")
def get_topics():
    return {"topics": ['topic1', 'topic2']}

class Topic(BaseModel):
    name: str
    
@app.post("/topics/{topic}")
def create_topic(topic):
    return {"Topic":topic}
