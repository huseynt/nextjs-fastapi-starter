from fastapi import FastAPI
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")
# import requests
# import tensorflow as tf
# import os

# file_request = {
#     "file_id": "1gsg1jcMuZ5kegl1u_CDUJ3hacqAvN0Tv",  # Faylın ID-si
#     "destination": "models/my_model.keras"  # Yüklənəcək yer
# }

# def download_file_from_drive(drive_file_id, destination):
#     """Google Drive-dan fayl endirmək üçün sadə funksiya"""
#     # Qovluğun mövcudluğunu yoxlayın və yaratmaq üçün:
#     directory = os.path.dirname(destination)
#     if not os.path.exists(directory):
#         os.makedirs(directory)  # Qovluğu yaradın

#     # Faylı yükləyin
#     url = f"https://drive.google.com/uc?id={drive_file_id}"
#     response = requests.get(url)
    
#     # Yüklənən məzmunu yoxlamaq
#     if response.status_code != 200:
#         raise RuntimeError("Google Drive bağlantısından fayl endirilemedi.")
    
#     # Faylın HTML səhifəsi olub olmadığını yoxlayın
#     if "html" in response.text:
#         raise RuntimeError("Yüklənən fayl HTML səhifəsidir. Faylın doğru yüklənmədiyini yoxlayın.")

#     # Faylın yazılması
#     with open(destination, "wb") as f:
#         f.write(response.content)
#     print(f"Fayl {destination} olaraq endirildi.")
#     return destination  # Yüklənmiş faylın yerini qaytar

# @app.get("/api/py/helloFastApi")
# def read_root():
#     # Faylı yükləyin
#     file_path = download_file_from_drive(file_request["file_id"], file_request["destination"])
    
#     try:
#         # Keras modelini yükləyin
#         model = tf.keras.models.load_model(file_path)
#         # Modelin strukturu və ya öyrədilmiş parametrləri haqqında məlumat verə bilərsiniz
#         model_summary = model.summary()  # Modelin ümumi xülasəsi

#     except Exception as e:
#         return {"error": f"Model yüklənərkən xəta baş verdi: {str(e)}"}

#     return {"message": "hello!", "model_summary": file_request["destination"]}



# @app.get("/api/py/hello")
# def hello_fast_api():
#     return {"message": "Hello from FastAPI"}

@app.get("/api/py/{name}")
def hello_fast_api_name(name: str):
    return {"message": f"Hello from FastAPI", "your_path": f"api/py/{name}", "name": name}


@app.post("/api/py/post")
def hello_fast_api_post(body: dict):    
    return {"message": "Hello from FastAPI POST", "body": body}


