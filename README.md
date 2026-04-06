# 🧠 Deepfake Image Detection App

This is a simple web application built using **Streamlit** and **TensorFlow** to detect whether an uploaded image is **REAL** or **FAKE (Deepfake)**.

---

## 📂 Files in this Folder

* `app.py` → Main application file
* `requirements.txt` → Required libraries
* `README.md` → Project description

---

## 🚀 How to Run

### 1. Open Terminal / PowerShell

Go to your project folder:

```
cd your_folder_path
```

---

### 2. (Optional) Create Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```
python -m pip install -r requirements.txt
```

---

### 4. Run the App

```
python -m streamlit run app.py
```

---

## 📸 How It Works

* Upload an image (JPG, PNG, JPEG)
* Image is resized to 128x128
* Model predicts:

  * ✅ REAL IMAGE
  * 🚨 FAKE IMAGE
* Shows confidence score

---

## ⚠️ Note

The model used in this project is **not trained**, so predictions are **random**.

To improve accuracy:

* Train the model on a dataset
* Save it as `model.h5`
* Load it in the app

---

## 🛠️ Requirements

Create a `requirements.txt` file with:

```
streamlit
tensorflow
numpy
pillow
```

---

## 👩‍💻 Author

Sneha

---

## 📌 Purpose

This project is for **educational and learning purposes only**.
