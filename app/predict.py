import tensorflow as tf
import numpy as np
from PIL import Image
import json


# Load model
model = tf.keras.models.load_model(
    "app/model/batik_model_final.keras"
)


# Load nama kelas
with open("app/model/classes.json", "r") as f:
    class_names = json.load(f)



def predict_image(image_path):

    # Buka gambar
    img = Image.open(image_path).convert("RGB")

    # Sesuai input training MobileNetV2
    img = img.resize((224, 224))


    img = np.array(
        img,
        dtype=np.float32
    )


    # PENTING:
    # Harus sama dengan training
    img = tf.keras.applications.mobilenet_v2.preprocess_input(
        img
    )


    img = np.expand_dims(
        img,
        axis=0
    )


    # Prediksi
    prediction = model.predict(
        img,
        verbose=0
    )[0]


    # Index tertinggi
    best_index = np.argmax(prediction)


    label = class_names[best_index]


    confidence = float(
        prediction[best_index] * 100
    )


    # Ambil Top 3 prediksi
    top3_index = np.argsort(prediction)[::-1][:3]


    top3 = []


    for i in top3_index:

        top3.append(
            {
                "label": class_names[i],
                "confidence": round(
                    float(prediction[i] * 100),
                    2
                )
            }
        )


    return label, confidence, top3