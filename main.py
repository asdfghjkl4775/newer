from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from starlette.responses import HTMLResponse
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn
from sklearn.cluster import KMeans
from PIL import Image
import numpy as np
import os
from random import sample


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

def ensure_directory_exists(path):
    os.makedirs(path, exist_ok=True)  # exist_ok=True 옵션을 통해 이미 디렉토리가 있으면 에러를 발생시키지 않음


@app.post("/upload/")
async def handle_upload(file: UploadFile = File(...)):
    upload_dir = "static/uploads"
    result_dir = "static/results"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    file_location = os.path.join(upload_dir, file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())

    output_path = os.path.join(result_dir, f"clustered_{file.filename}")
    # Assuming save_clustered_image is defined elsewhere and works correctly
    save_clustered_image(file_location, output_path)

    return {"info": "Uploaded and Processed", "result_image": f"/static/results/clustered_{file.filename}"}

def save_clustered_image(file_path, output_path):
    image = Image.open(file_path)
    data = np.array(image)
    reshaped_data = data.reshape((-1, 3))
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(reshaped_data)
    clustered_data = kmeans.cluster_centers_[kmeans.labels_]
    clustered_image = clustered_data.reshape(data.shape).astype(np.uint8)
    clustered_result = Image.fromarray(clustered_image)
    clustered_result.save(output_path)


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
    emotions = ["행복", "기쁨", "사랑", "세련됨", "감각적", "호기심", "경외심", "슬픔", "미움", "걱정", "혼란", "공포", "노여움", "욕심", "동정"]
    fin = sample(emotions, 3) 
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
