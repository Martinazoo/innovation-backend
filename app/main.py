from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import Base, engine
from sqlalchemy.orm import Session
import models
import routers
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routers.auth_router)
app.include_router(routers.users_router)
app.include_router(routers.route_router)