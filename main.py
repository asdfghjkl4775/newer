from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from starlette.responses import HTMLResponse


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/artist_signup", response_class=HTMLResponse)
async def artist_signup(request: Request):
    return templates.TemplateResponse("artist_signup.html", {"request": request})

@app.get("/exhibition", response_class=HTMLResponse)
async def exhibition(request: Request):
    return templates.TemplateResponse("exhibition.html", {"request": request})

@app.get("/exhibition_detail", response_class=HTMLResponse)
async def exhibition_detail(request: Request):
    return templates.TemplateResponse("exhibition_detail.html", {"request": request})

@app.get("/gallery", response_class=HTMLResponse)
async def gallery(request: Request):
    return templates.TemplateResponse("gallery.html", {"request": request})

@app.get("/gallery_itemdetail", response_class=HTMLResponse)
async def gallery_itemdetail(request: Request):
    return templates.TemplateResponse("gallery_itemdetail.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/login_complete", response_class=HTMLResponse)
async def login_complete(request: Request):
    return templates.TemplateResponse("login_complete.html", {"request": request})

@app.get("/mypage", response_class=HTMLResponse)
async def mypage(request: Request):
    return templates.TemplateResponse("mypage.html", {"request": request})

@app.get("/community_main", response_class=HTMLResponse)
async def community_main(request: Request):
    return templates.TemplateResponse("community_main.html", {"request": request})

@app.get("/artist_detail", response_class=HTMLResponse)
async def artist_detail(request: Request):
    return templates.TemplateResponse("artist_detail.html", {"request": request})

@app.get("/ai_recomm", response_class=HTMLResponse)
async def ai_recomm(request: Request):
    fin = ["추천 단어1", "추천 단어2", "추천 단어3"]
    return templates.TemplateResponse("ai_recomm.html", {"request": request, "fin": fin})

@app.get("/interior_detail_final", response_class=HTMLResponse)
async def interior_detail_final(request: Request):
    return templates.TemplateResponse("interior_detail_final.html", {"request": request})

@app.get("/enroll", response_class=HTMLResponse)
async def enroll(request: Request):
    return templates.TemplateResponse("enroll.html", {"request": request})

@app.get("/user_signup", response_class=HTMLResponse)
async def user_signup(request: Request):
    return templates.TemplateResponse("user_signup.html", {"request": request})



@app.get("/artistinform", response_class=HTMLResponse)
async def artistinform(request: Request):
    return templates.TemplateResponse("artistinform.html", {"request": request})


@app.get("/imci", response_class=HTMLResponse)
async def imci(request: Request):
    return templates.TemplateResponse("imci.html", {"request": request})



@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})



# Run the app with `uvicorn`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
