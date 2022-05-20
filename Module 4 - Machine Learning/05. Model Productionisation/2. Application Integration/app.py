import streamlit as st
import numpy as np
from pickle import load

lr_model = load(open('models/lr_model.pkl', 'rb'))

sl = st.text_input("Sepal Length", placeholder="Enter value in cm")
sw = st.text_input("Sepal Width", placeholder="Enter value in cm")
pl = st.text_input("Petal Length", placeholder="Enter value in cm")
pw = st.text_input("Petal Width", placeholder="Enter value in cm")

btn_click = st.button("Predict")

if btn_click == True:
    if sl and sw and pl and pw:
        arr = np.array([float(sl), float(sw), float(pl), float(pw)])
        pred = lr_model.predict(arr.reshape(1, -1))
        st.success(pred)
    else:
        st.error("Enter the values properly.")