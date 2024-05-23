from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database import schemas
from database.database import get_db
from handlers.tags import get_tags_db, create_tag_db, delete_tag_db

router = APIRouter()


@router.get('/', status_code=200)
async def get_tags(db: AsyncSession = Depends(get_db)):
    return await get_tags_db(db=db)


@router.post('/create', status_code=201)
async def create_tag(tag_data: schemas.TagBase, db: AsyncSession = Depends(get_db)):
    return await create_tag_db(db=db, tag_data=tag_data)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_tag(tag_data: schemas.DeleteBase, db: AsyncSession = Depends(get_db)):
    return await delete_tag_db(db=db, tag_data=tag_data)

