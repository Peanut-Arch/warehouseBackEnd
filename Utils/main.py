from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Utils.db import db
from contextlib import asynccontextmanager
from Routers.Users import User_router
from Routers.Items import Items_router


#################################################################### Setup
@asynccontextmanager
async def lifespan(app:FastAPI):
    await db.connect()
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(User_router)
app.include_router(Items_router)

#################################################################### Setup Done

#################################################################### A must keep
@app.get("/")
async def root():
    return {"hello":"world"}


