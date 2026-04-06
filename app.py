import streamlit as st
import numpy as np
from PIL import Image
import random   # ✅ added (no tensorflow)

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
# Prediction (Demo Mode)
# ----------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = preprocess(image)

    # ✅ Random prediction (since no trained model)
    prediction = random.random()

    if prediction > 0.5:
        st.error("🚨 FAKE IMAGE (Deepfake)")
    else:
        st.success("✅ REAL IMAGE")

    st.write(f"Confidence Score: {prediction:.4f}")
