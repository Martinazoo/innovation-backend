from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import Base, engine
from sqlalchemy.orm import Session
import models
import routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(routers.auth_router)
app.include_router(routers.users_router)