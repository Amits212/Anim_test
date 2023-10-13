from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/login')
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post('/content')
async def all_content(request: Request):
    return HTMLResponse(request)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
