from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from . import settings

app = FastAPI()

@app.get("/")
async def homepage(request: Request):
	return settings.TEMPLATES.TemplateResponse("home.html", {"request": request})

@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello_name(name: str):
	return f"<p>Hello, {name}!</p>"
