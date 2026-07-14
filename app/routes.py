import os

from flask import render_template, request
from flask import render_template
from app import app
from app.predict import predict_image
from app.batik_info import BATIK_INFO

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return "File tidak ditemukan"

    file = request.files["image"]

    if file.filename == "":
        return "Tidak ada file yang dipilih"

    upload_folder = app.config["UPLOAD_FOLDER"]

    os.makedirs(upload_folder, exist_ok=True)

    image_path = os.path.join(upload_folder, file.filename)

    file.save(image_path)

    label, confidence, top3 = predict_image(image_path)
    info = BATIK_INFO.get(label, {
        "nama": label,
        "daerah": "-",
        "filosofi": "-",
        "deskripsi": "-"
    })

    return render_template(
    "result.html",
    label=label,
    confidence=round(confidence, 2),
    image=file.filename,
    info=info,
    top3=top3
)