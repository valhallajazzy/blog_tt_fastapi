from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.exceptions import HTTPException

from database.models import Category
from database.schemas import CategoryBase, DeleteBase


async def create_category_db(db: AsyncSession, category_data: CategoryBase):
    if await db.scalar(select(Category).where(Category.category_name == category_data.category_name)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category {category_data.category_name} already exist"
        )
    category = Category(category_name=category_data.category_name)
    db.add(category)
    await db.commit()
    return {
        "id": category.id,
        "category_name": category.category_name,
    }


async def get_category_db(db: AsyncSession):
    result = await db.execute(select(Category))
    return result.scalars().all()


async def delete_category_db(db: AsyncSession, category_data: DeleteBase):
    category = await db.scalar(select(Category).where(Category.id == category_data.id))
    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category not found!"
        )
    await db.delete(category)
    await db.commit()

