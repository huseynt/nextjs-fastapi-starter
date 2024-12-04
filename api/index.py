import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
from PIL import Image, UnidentifiedImageError
import requests
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Bütün domenlərə icazə ver. Təhlükəsizlik üçün dəyişdirə bilərsiniz.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model dosya yolu ve yüklenmesi
model_path = os.path.abspath(r"E:\nextjs-fastapi-starter-main\model_fire.keras")
if os.path.exists(model_path):
    print(f"Model bulundu: {model_path}")
else:
    raise RuntimeError(f"Model dosyas bulunamad: {model_path}")

try:
    model = tf.keras.models.load_model(model_path, safe_mode=False)
    print("Model baaryla yüklendi.")
except Exception as e:
    print(f"Model yüklenemedi: {e}")
    raise RuntimeError(f"Model yüklenemedi: {e}")

# Sınıf etiketleri ve güvenlik önerileri
class_labels = ['Fire', 'Non-Fire']
fire_tips = {
    'Fire': "Yangn tespit edildi! Ltfen yetkililere haber verin.",
    'Non-Fire': "Gvende grnyorsunuz. Ancak, phe varsa etraf kontrol edin."
}

# Tahmin yapılacak görselin URL formatında alınması
class ImageURL(BaseModel):
    url: str

# Tahmin işlemi
@app.post("/api/py/predict")
def predict_fire(image_data: ImageURL):
    try:
        # Görseli URL'den indirme
        response = requests.get(image_data.url)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Görsel URL'ine ulalamad.")
        
        try:
            img = Image.open(BytesIO(response.content))
        except UnidentifiedImageError:
            raise HTTPException(status_code=400, detail="Geersiz görsel format.")

        # Görseli işleme (RGB'ye çevirme, boyutlandırma)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img = img.resize((224, 224))
        img_array = np.array(img) / 255.0  # Normalizasyon
        img_array = np.expand_dims(img_array, axis=0)

        # Modelden tahmin alma
        prediction = model.predict(img_array)
        predicted_index = np.argmax(prediction)
        predicted_class = class_labels[predicted_index]
        confidence = float(prediction[0][predicted_index])
        tips = fire_tips[predicted_class]

        # Tahmin sonucu döndürme
        return {
            "prediction": predicted_class,
            "confidence": f"{confidence:.2f}",
            "tips": tips
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Tahmin ilemi srasnda hata olutu: {e}")

# Ana sayfa
# @app.get("/")
# def read_root():
#     return {"message": "Fire and Non-Fire snflandrma API'si calisiyor!"}


@app.get("/api/py/hello")
def read_root():
    return {"message": "Fire and Non-Fire siniflandirma API'si calisiyor!"}