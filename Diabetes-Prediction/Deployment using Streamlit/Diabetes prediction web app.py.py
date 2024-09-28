# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:20:22 2023

@author: Shantanu Mishra
"""


import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open("C:\Users\Shantanu Mishra\OneDrive\Desktop\Deploying ML\trained_model.sav",'rb'))

# creating a function for prediction

def diabetes_prediction(input_data):
   

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
def main():
    
    #giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from from the user
    Pregnancies = st.text_input('No of Pregnancies')
    Glucose = st.text_input('Enter Glucose Level')
    BloodPressure = st.text_input('Enter the Blood Pressure Level ')
    SkinThickness = st.text_input('Enter the Skin Thickness ')
    Insulin = st.text_input('Enter the Insulin level ')
    BMI = st.text_input('Enter the BMI ')
    DiabetesPedigreeFunction = st.text_input('Enter the Diabetes Pedigree Function ')
    Age = st.text_input('Enter the Age of Person ')
    
    
    # code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
