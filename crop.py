import streamlit as st
import pandas as pd
import numpy as np
import sklearn

sklearn_version = sklearn.__version__.split('.')
if int(sklearn_version[0]) < 0 or (int(sklearn_version[0]) == 0 and int(sklearn_version[1]) < 24):
    raise ImportError("The scikit-learn version is incompatible. Please upgrade to scikit-learn 0.24 or later.")

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# Load the data
data = pd.read_csv('Crop_recommendation.csv')

# Feature selection
features = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
target = data['label']

# Train the model
knn = KNeighborsClassifier()
knn.fit(features, target)

# Streamlit App
st.title('Crop Recommendation')

# User input for crop features
st.subheader('Enter Crop Data:')
N = st.number_input('Nitrogen', value=0, step=1)
P = st.number_input('Phosphorus', value=0, step=1)
K = st.number_input('Potassium', value=0, step=1)
temperature = st.number_input('Temperature', value=0.0)
humidity = st.number_input('Humidity', value=0.0)
ph = st.number_input('pH', value=0.0)
rainfall = st.number_input('Rainfall', value=0.0)

# Button to trigger prediction
if st.button('Predict'):
    if N == 0 and P == 0 and K == 0 and temperature == 0.0 and humidity == 0.0 and ph == 0.0 and rainfall == 0.0:
        st.warning("Please enter crop data.")
    else:
        # Predict for user input
        new_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        prediction = knn.predict(new_data)

        # Display prediction result
        st.subheader('Crop Prediction')
        st.write("Prediction: ", prediction[0])
