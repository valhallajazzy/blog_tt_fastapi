import os

from fastapi import FastAPI

from routers.authors import router as author_routers
from routers.posts import router as post_routers
from routers.categories import router as category_routers
from routers.tags import router as tag_routers

app = FastAPI()


app.include_router(
    router=author_routers,
    prefix='/authors'
)


app.include_router(
    router=post_routers,
    prefix='/posts'
)


app.include_router(
    router=category_routers,
    prefix='/categories'
)


app.include_router(
    router=tag_routers,
    prefix='/tags'
)


if __name__ == '__main__':
    os.system("uvicorn main:app --host 0.0.0.0 --port 8004")