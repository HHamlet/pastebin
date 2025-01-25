from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from db.core.config import CONNECTION_STRING

engine = create_async_engine(CONNECTION_STRING, echo=True, pool_size=10, max_overflow=20)
async_session = async_sessionmaker(engine, expire_on_commit=False)
