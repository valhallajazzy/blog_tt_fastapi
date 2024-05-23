from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database import schemas
from database.database import get_db
from handlers.authors import get_authors_db, create_author_db, update_authors_db, delete_author_db

router = APIRouter()


@router.get('/', status_code=200)
async def get_clients(db: AsyncSession = Depends(get_db)):
    return await get_authors_db(db=db)


@router.post('/create', status_code=201)
async def create_author(author_data: schemas.AuthorBase, db: AsyncSession = Depends(get_db)):
    return await create_author_db(db=db, author_data=author_data)


@router.patch('/update', status_code=200)
async def update_author(author_data: schemas.AuthorBase, db: AsyncSession = Depends(get_db)):
    return await update_authors_db(db=db, author_data=author_data)


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(author_data: schemas.DeleteBase, db: AsyncSession = Depends(get_db)):
    return await delete_author_db(db=db, author_data=author_data)

