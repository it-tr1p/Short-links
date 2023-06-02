from typing import Union

from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, \
    create_async_engine
from sqlalchemy.orm import sessionmaker


def build_async_engine(url: Union[URL, str]) -> AsyncEngine:
    return create_async_engine(
        url=url, echo=True, pool_pre_ping=True, future=True
    )


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(engine=engine, class_=AsyncSession)


