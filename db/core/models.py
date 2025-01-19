from sqlalchemy.orm import DeclarativeBase,  Mapped, mapped_column
from sqlalchemy import String, Text


class PastModel(DeclarativeBase):
    __tablename__ = "past"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String(50), unique=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    def __repr__(self):
        return f"PastModel(id={self.id}, content={self.content} , slug={self.slug})"
