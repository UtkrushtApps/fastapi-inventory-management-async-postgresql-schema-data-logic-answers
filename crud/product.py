from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from models.product import Product

async def create_product(db: AsyncSession, *, name: str, description: Optional[str], quantity: int, price: float) -> Product:
    product = Product(name=name, description=description, quantity=quantity, price=price)
    db.add(product)
    try:
        await db.commit()
        await db.refresh(product)
    except IntegrityError:
        await db.rollback()
        raise ValueError("Product with this name already exists.")
    return product

async def get_all_products(db: AsyncSession) -> List[Product]:
    result = await db.execute(select(Product))
    return result.scalars().all()
