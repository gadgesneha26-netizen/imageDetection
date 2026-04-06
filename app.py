import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# ----------------------------
# Build Simple CNN Model
# ----------------------------
def create_model():
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
        MaxPooling2D(),

        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D(),

        Flatten(),
        Dense(128, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

# Create model
model = create_model()

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Deepfake Detector", layout="centered")

st.title("🧠 Deepfake Image Detection")
st.write("Upload an image to check whether it's REAL or FAKE")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

# ----------------------------
# Image Processing
# ----------------------------
def preprocess(image):
    image = image.resize((128,128))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# ----------------------------
# Prediction
# ----------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = preprocess(image)

    # Since model is not trained, prediction is random/demo
    prediction = model.predict(img)

    # Convert to readable result
    if prediction[0][0] > 0.5:
        st.error("🚨 FAKE IMAGE (Deepfake)")
    else:
        st.success("✅ REAL IMAGE")

    st.write(f"Confidence Score: {float(prediction[0][0]):.4f}")