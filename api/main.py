from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from . import settings

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
	return settings.TEMPLATES.TemplateResponse("home.html", {"request": request})

@app.get("/hello", response_class=HTMLResponse)
async def hello(request: Request):
	return settings.TEMPLATES.TemplateResponse("hello.html", {"request": request, "name": "World"})

@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello_name(request: Request, name: str):
	return settings.TEMPLATES.TemplateResponse("hello.html", {"request": request, "name": name})
