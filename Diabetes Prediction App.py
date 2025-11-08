# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 15:24:38 2025

@author: HP
"""

import os
import pickle 
import streamlit as st
import numpy as np

# Load Model and Scaler
model_path = os.path.join(os.path.dirname(__file__),"diabeties_nb_stacking.sav")
scaler_path = os.path.join(os.path.dirname(__file__),"scaler.pkl")

try:
    model = pickle.load(open(model_path,"rb"))
    scaler = pickle.load(open(scaler_path,"rb"))
except FileNotFoundError:
    st.error("Model File Not Found")
    st.stop()
    
def diabetes_prediction(input_data):
    input_data_as_np_array = np.asarray(input_data).reshape(1,-1)
    scaled_data = scaler.transform(input_data)
    prediction =  model.predict(scaled_data)
    
    if prediction[0] == 1:
        return "The Preson is Likely to have Diabeties"
    else:
        return "The preson is likely not Diabetic"
    
def main():
    st.title("Diabetes Prediction using Stacking Ensemble (Naive Bayes Meta-Model)")
    st.write("Enter the medical parameters below to predict the likelihood of diabetes.")
    
    Pregnancies = st.number_input("Pregnancies")
    Glucose = st.number_input("Glucose Level")
    BloodPressure = st.number_input("Blood Pressure")
    SkinThickness = st.number_input("Skin Thickness")
    insulin = st.number_input("Insulin Level")
    BMI = st.number_input("BMI (Body Mass index)")
    DiabetesPredigreeFunction = st.number_input("Diabeties Predigree Function")
    Age = st.number_input("Age")
    
    diagonosis = ""
    if st.button("Predict Diabetes"):
        diagonosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,insulin,BMI,DiabetesPredigreeFunction,Age])
        
    st.success(diagonosis)
    
if __name__ == "__main__":
    main()