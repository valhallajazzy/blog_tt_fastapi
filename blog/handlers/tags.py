from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.exceptions import HTTPException

from database.models import Tag
from database.schemas import TagBase, DeleteBase


async def create_tag_db(db: AsyncSession, tag_data: TagBase):
    if await db.scalar(select(Tag).where(Tag.title == tag_data.title)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Tag {tag_data.title} already exist"
        )
    tag = Tag(title=tag_data.title)
    db.add(tag)
    await db.commit()
    return {
        "id": tag.id,
        "title": tag.title,
    }


async def get_tags_db(db: AsyncSession):
    result = await db.execute(select(Tag))
    return result.scalars().all()


async def delete_tag_db(db: AsyncSession, tag_data: DeleteBase):
    tag = await db.scalar(select(Tag).where(Tag.id == tag_data.id))
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Tag not found!"
        )
    await db.delete(tag)
    await db.commit()