from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database import schemas
from database.database import get_db
from handlers.posts import get_posts_db, create_post_db, update_post_db, delete_post_db

router = APIRouter()


@router.get('/', status_code=200)
async def get_posts(db: AsyncSession = Depends(get_db)):
    return await get_posts_db(db=db)


@router.post('/create', status_code=201)
async def create_post(post_data: schemas.PostBase, db: AsyncSession = Depends(get_db)):
    return await create_post_db(db=db, post_data=post_data)


@router.patch('/update', status_code=200)
async def update_post(post_data: schemas.PostUpdate, db: AsyncSession = Depends(get_db)):
    return await update_post_db(db=db, post_data=post_data)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_data: schemas.DeleteBase, db: AsyncSession = Depends(get_db)):
    return await delete_post_db(db=db, post_data=post_data)