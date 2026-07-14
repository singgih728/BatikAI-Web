# BatikAI-Web
UAS KECERDASAN BUATAN
BatikAI Web - Klasifikasi Motif Batik Menggunakan CNN Transfer Learning

---

# Bahasa Pemrograman yang Digunakan

* Python 3.x
* HTML5
* CSS3
* JavaScript

---

# Framework, Library, dan API yang Digunakan

## Framework

* Flask

## Deep Learning Framework

* TensorFlow
* Keras

## Library

* NumPy
* Pillow (PIL)
* Matplotlib
* Scikit-learn
* JSON
* OS

## Model AI

* MobileNetV2 (Transfer Learning)

## API

* Tidak menggunakan API eksternal.

---

# Fungsi dan Fitur Proyek

### Fungsi

Aplikasi digunakan untuk melakukan klasifikasi otomatis terhadap gambar motif batik Indonesia sehingga pengguna dapat mengetahui jenis motif batik yang diunggah.

### Fitur

* Upload gambar batik
* Prediksi motif batik menggunakan AI
* Menampilkan nama motif batik
* Menampilkan nilai confidence (persentase keyakinan model)
* Menampilkan Top 3 hasil prediksi
* Antarmuka berbasis web yang mudah digunakan
* Model tersimpan dalam format `.keras`
* Penyimpanan nama kelas menggunakan `classes.json`

---

# Kelebihan Proyek

* Menggunakan metode Transfer Learning sehingga proses pelatihan lebih cepat dibanding membangun model CNN dari awal.
* Model MobileNetV2 memiliki ukuran relatif ringan sehingga cocok digunakan pada aplikasi web.
* Proses prediksi berlangsung secara cepat setelah gambar diunggah.
* Struktur proyek sederhana sehingga mudah dikembangkan.
* Mudah diintegrasikan dengan framework Flask.
* Dapat dikembangkan menjadi aplikasi edukasi batik Indonesia.

---

# Kekurangan Proyek (Bug / Warning)

* Nilai confidence pada beberapa gambar masih rendah karena beberapa motif batik memiliki karakteristik visual yang mirip.
* Akurasi model sangat dipengaruhi oleh kualitas dan jumlah dataset yang digunakan.
* Sistem hanya mengenali motif batik yang terdapat pada dataset pelatihan.
* Belum tersedia fitur riwayat prediksi.
* Belum mendukung prediksi banyak gambar (batch prediction).
* Belum diimplementasikan proses fine tuning lanjutan untuk meningkatkan performa model.
* Tampilan aplikasi masih sederhana dan belum responsif secara penuh pada perangkat mobile.

---

# Dataset

Dataset yang digunakan merupakan dataset citra motif batik Indonesia.

**Link Dataset Kaggle:**

[https://www.kaggle.com/datasets/stevennugroho/batik-dataset(https://www.kaggle.com/datasets/hendryhb/batik-nusantara-batik-indonesia-dataset?resource=download)

> **Catatan:** Apabila pada proses pelatihan digunakan dataset yang telah dimodifikasi (misalnya penambahan folder train/test atau pengurangan kelas), maka struktur dataset pada proyek ini merupakan hasil pengolahan dari dataset asli tersebut.

---

# Penjelasan Dataset

Dataset terdiri dari kumpulan citra motif batik Indonesia yang telah dikelompokkan berdasarkan kelas masing-masing. Setiap folder merepresentasikan satu jenis motif batik.

Pada proyek ini digunakan **20 kelas motif batik**, yaitu:

1. Aceh_Pintu_Aceh
2. Bali_Barong
3. Bali_Merak
4. DKI_Ondel_Ondel
5. JawaBarat_Megamendung
6. JawaTimur_Pring
7. Kalimantan_Dayak
8. Lampung_Gajah
9. Madura_Mataketeran
10. Maluku_Pala
11. NTB_Lumbung
12. Papua_Asmat
13. Papua_Cendrawasih
14. Papua_Tifa
15. Solo_Parang
16. SulawesiSelatan_Lontara
17. SumateraBarat_Rumah_Minang
18. SumateraUtara_Boraspati
19. Yogyakarta_Kawung
20. Yogyakarta_Parang

Dataset dibagi menjadi dua bagian utama:

* **Training Set** → digunakan untuk melatih model CNN.
* **Testing Set** → digunakan untuk menguji performa model setelah proses pelatihan selesai.

Seluruh gambar diproses dengan ukuran **224 × 224 piksel** dan menggunakan preprocessing **MobileNetV2** sebelum dimasukkan ke dalam model.

---

# Cara Menjalankan Proyek

1. Clone atau download repository.
2. Install seluruh dependency:

```bash
pip install -r requirements.txt
```

atau

```bash
pip install flask tensorflow pillow numpy matplotlib scikit-learn
```

3. Pastikan file berikut berada pada folder:

```
app/model/
├── batik_model_final.keras
└── classes.json
```

4. Jalankan aplikasi:

```bash
python run.py
```

5. Buka browser dan akses:

```
http://127.0.0.1:5000
```

---

# Struktur Proyek

```
BatikAI_Web/
│
├── run.py
├── requirements.txt
├── README.md
│
└── app/
    ├── predict.py
    ├── routes.py
    ├── model/
    │   ├── batik_model_final.keras
    │   └── classes.json
    ├── static/
    └── templates/
```

---

# Pengembang

**Nama:** Singgih Rohniadi

**Program Studi:** Teknik Informatika
