from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
     # cross-origin resource sharing -> needed such that requests go through when different server
from api.routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)