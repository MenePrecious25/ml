import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.mobilenet import decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
# from tensorflow.python.platform import _pywrap_tf2
import numpy as np

st.title("Weather Image Classification")

# Load the models
mobilenet_model = load_model('model_15-0.57.h5')


# Upload image
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    img = image.load_img(uploaded_file, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.write("")


    if st.button('predict'):
    # Make predictions
        mobilenet_pred = np.argmax(mobilenet_model.predict(img_array), axis=1)[0]
        if mobilenet_pred == 0:
          mobilenet_pred = "Cloudy"
        elif mobilenet_pred == 1:
          mobilenet_pred = "Lighening"
        elif mobilenet_pred == 2:
          mobilenet_pred = "Rain"
        elif mobilenet_pred == 3:
          mobilenet_pred = "Rainbow"
        elif mobilenet_pred == 4:
          mobilenet_pred = "Snow"
        elif mobilenet_pred == 5:
          mobilenet_pred = "Sunrise"
        elif mobilenet_pred == 6:
          mobilenet_pred = "Sunny"
        st.write(f"MobileNet Prediction: {mobilenet_pred}")
