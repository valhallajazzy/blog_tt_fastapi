from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.exceptions import HTTPException

from database.models import Post, Author, Category
from database.schemas import PostUpdate, PostBase, DeleteBase


async def create_post_db(db: AsyncSession, post_data: PostBase):
    author = await db.scalar(select(Author).where(Author.id == post_data.author_id))
    category = await db.scalar(select(Category).where(Category.id == post_data.category_id))
    if not (author or category):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Incorrect author_id or category_id"
        )
    post = Post(title=post_data.title)
    post.text = post_data.text
    post.author_id = post_data.author_id
    post.category_id = post.category_id
    db.add(post)
    await db.commit()
    return {
        "id": post.id,
        "title": post.title,
        "author_id": post.author_id,
        "category_id": post.category_id
    }


async def get_posts_db(db: AsyncSession):
    return db.execute(select(Post).all())


async def update_post_db(db: AsyncSession, post_data: PostUpdate):
    post = await db.scalar(select(Post).where(Post.id == post_data.id))
    if not post:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Post is not exist!"
        )
    for name, value in post_data.model_dump(exclude_unset=True).items():
        setattr(post, name, value)
    await db.commit()
    return {
        "title": post.title,
        "text": post.text,
    }


async def delete_post_db(db: AsyncSession, post_data: DeleteBase):
    post = await db.scalar(select(Post).where(Post.id == post_data.id))
    if not post:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Post not found!"
        )
    await db.delete(post)
    await db.commit()


