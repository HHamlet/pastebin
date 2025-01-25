from sqlalchemy.orm import DeclarativeBase,  Mapped, mapped_column
from sqlalchemy import String, Text, DateTime
from datetime import datetime


class BaseModel(DeclarativeBase):
    pass


class PastModel(BaseModel):
    __tablename__ = "past"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"PastModel(id={self.id}, content={self.content} , slug={self.slug}, created_at={self.created_at})"
