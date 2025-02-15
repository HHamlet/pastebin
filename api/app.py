import uvicorn
from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.exc import NoResultFound
from sqlalchemy.sql import select
from db.db import async_session
from db.core.models import PastModel
from pygments.formatters import HtmlFormatter
import string
import random
import markdown

app = FastAPI()

templates = Jinja2Templates(directory="api/templates")


def generate_slug(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/create", response_class=HTMLResponse)
async def create_paste(request: Request, content: str = Form(...)):
    if not content.strip():
        return templates.TemplateResponse(
            "index.html", {"request": request, "error": "Content cannot be empty"}
        )

    slug = generate_slug()

    async with async_session() as session:
        async with session.begin():
            slug_find = await session.scalars(select(PastModel).where(PastModel.slug == slug))
            while slug_find.all():
                print(slug_find.all())
                slug = generate_slug()
            statement = PastModel(slug=slug, content=content)
            session.add(statement)
            session.commit()

    paste_url = f"http://127.0.0.1:8090/{slug}"
    return templates.TemplateResponse(
        "index.html", {"request": request, "success": "Paste created!", "url": paste_url}
    )


@app.get("/{slug}", response_class=HTMLResponse)
async def get_paste(request: Request, slug: str):
    async with async_session() as session:
        async with session.begin():
            statement = select(PastModel.content).where(PastModel.slug == slug)
            temp = await session.scalars(statement)
            try:
                result = temp.one()
            except NoResultFound:
                raise HTTPException(status_code=404, detail="Paste not found")
            html_content = markdown.markdown(result, extensions=["fenced_code", "codehilite"])
            formatter = HtmlFormatter(style="friendly")
            code_styles = formatter.get_style_defs('.codehilite')

            return templates.TemplateResponse("paste.html", {"request": request, "slug": slug,
                                                             "content": html_content,
                                                             "code_styles": code_styles})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8090)
