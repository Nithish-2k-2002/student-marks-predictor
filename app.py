import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("Students Mark Predictor")

study_hours = st.slider("Hours Studied ", 0.0, 10.0, 2.5)

x = np.array([[1], [2], [3], [4], [5]])  # array list

y = np.array([35, 45, 50, 60, 70])

model = LinearRegression()
model.fit(x, y)

predicted_marks = model.predict([[study_hours]])

st.write(f"Esitmated Marks : **{predicted_marks[0]:.2f}**")
