import streamlit as st
import cv2
import matplotlib.pyplot as plt
import numpy as np

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    # Convert the uploaded file to a numpy array
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Convert the BGR image to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Convert to grayscale and apply median blur to reduce image noise
    grayimg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    grayimg = cv2.medianBlur(grayimg, 5)

    # Get the edges
    edges = cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Convert to a cartoon version
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Display original image
    st.image(img, caption='Original Image')

    # Display cartoon image
    st.image(cartoon, caption='Cartoon Image')
