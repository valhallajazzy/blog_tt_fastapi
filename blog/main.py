import os

from fastapi import FastAPI

from routers.authors import router as author_routers

app = FastAPI()


app.include_router(
    router=author_routers,
    prefix='/authors'
)

