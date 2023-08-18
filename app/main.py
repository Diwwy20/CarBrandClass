from fastapi import FastAPI, Request
from app.code import callAPI
import pickle
import os

app = FastAPI()

# model = pickle.load(open(r'../model/model_genhog.pkl', 'rb'))
model = pickle.load(open(os.getcwd() + r'/model/model_genhog.pkl', 'rb'))


@app.get("/")
def root():
    return {"message": "This is my api"}

@app.post("/api/carbrand")
async def read_str(data: Request):
    json = await data.json()
    image_str = json['img_base64']
    car_brand = callAPI(image_str, model)

    return {"Brand": car_brand}