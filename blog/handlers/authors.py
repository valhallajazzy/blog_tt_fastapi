from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.exceptions import HTTPException

from database.models import Author
from database.schemas import AuthorBase, DeleteBase


async def create_author_db(db: AsyncSession, author_data: AuthorBase):
    if await db.scalar(select(Author).where(Author.email == author_data.email)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Author {author_data.email} already exist"
        )
    author = Author(email=author_data.email)
    author.first_name = author_data.first_name
    author.last_name = author_data.last_name
    db.add(author)
    await db.commit()
    return {
        "id": author.id,
        "first_name": author.first_name,
        "last_name": author.last_name,
        "email": author.email
    }


async def get_authors_db(db: AsyncSession):
    return db.execute(select(Author).all())


async def update_authors_db(db: AsyncSession, author_data: AuthorBase):
    author = await db.scalar(select(Author).where(Author.email == author_data.email))
    if not author:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Author {author_data.email} not found!"
        )
    for name, value in author_data.model_dump(exclude_unset=True).items():
        setattr(author, name, value)
    await db.commit()
    return {
        "id": author.id,
        "first_name": author.first_name,
        "last_name": author.last_name,
        "email": author.email
    }


async def delete_author_db(db: AsyncSession, author_data: DeleteBase):
    author = await db.scalar(select(Author).where(Author.id == author_data.id))
    if not author:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Author {author_data.id} not found!"
        )
    await db.delete(author)
    await db.commit()