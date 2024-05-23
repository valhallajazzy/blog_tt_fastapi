import os

from fastapi import FastAPI

from routers.authors import router as author_routers
from routers.posts import router as post_routers

app = FastAPI()


app.include_router(
    router=author_routers,
    prefix='/authors'
)


app.include_router(
    router=post_routers,
    prefix='/posts'
)



