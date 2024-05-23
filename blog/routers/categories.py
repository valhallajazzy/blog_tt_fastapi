from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database import schemas
from database.database import get_db
from handlers.categories import get_category_db, create_category_db, delete_category_db

router = APIRouter()


@router.get('/', status_code=200)
async def get_categories(db: AsyncSession = Depends(get_db)):
    return await get_category_db(db=db)


@router.post('/create', status_code=201)
async def create_category(category_data: schemas.CategoryBase, db: AsyncSession = Depends(get_db)):
    return await create_category_db(db=db, category_data=category_data)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_data: schemas.DeleteBase, db: AsyncSession = Depends(get_db)):
    return await delete_category_db(db=db, category_data=category_data)


