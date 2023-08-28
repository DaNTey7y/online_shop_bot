from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import User, Section, Product, Operation


async def get_user_data(session: AsyncSession, required_id: int):
    user_data = await session.execute(
        select(User).where(User.user_id == required_id)
    )
    return user_data.scalars().one()


async def get_sections(session: AsyncSession):
    result = await session.execute(select(Section))
    return result.scalars().all()


async def get_goods_by_section(session: AsyncSession, section: int):
    result = await session.execute(select(Product).where(Product.section_id == section))
    return result.scalars().all()


async def get_section_data(session: AsyncSession, section: int):
    result = await session.execute(select(Section).where(Section.section_id == section))
    return result.scalars().one()


async def get_product(session: AsyncSession, product_id: int):
    result = await session.execute(
        select(Product).where(Product.product_id == product_id)
    )
    return result.scalars().one()


async def get_user_history(session: AsyncSession, user_id: int):
    result = await session.execute(
        select(Operation).where(Operation.user_id == user_id)
    )
    return result.scalars().all()
