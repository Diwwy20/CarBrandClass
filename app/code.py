import requests

label_mapping = {0: "Audi", 1: "Hyundai Creta", 2: "Mahindra Scorpio",
                3: "Rolls Royce", 4: "Swift", 5: "Tata Safari",
                6:"Toyota Innova"}

url = "http://172.17.0.1:8080/api/genhog"

def callAPI(img, model):
    try:
        params = {"img_base64": img}

        response = requests.get(url, json=params)

        if response.status_code == 200:
            res = response.json()
            hogList = list(res.values())
            car_predict = model.predict(hogList)
            car_brand = label_mapping.get(car_predict[0])
            return car_brand
        else:
            return {"error": f"API error number code : {response.status_code}"}
    except Exception as ex:
        return {"error": f" message: {str(ex)}"}