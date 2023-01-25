from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from core.database import engine
from core import base, database

# add routers
import db_example


# all models -> db tables
base.Base.metadata.create_all(engine)


app = FastAPI(title=settings.PROJECT_NAME)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# db
get_db = database.get_db


app.include_router(db_example.router)


@app.get('/')
def index():
    return {"hello": "world"}
