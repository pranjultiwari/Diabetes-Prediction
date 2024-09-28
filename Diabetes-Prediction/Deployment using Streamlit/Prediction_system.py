# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:18:07 2023

@author: Shantanu Mishra
"""
8
import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open(r'C:\Users\Shantanu Mishra\OneDrive\Desktop\Deploying ML\trained_model.sav','rb'))

a = int(input("Enter the no of Pregenencies: "))
b = int(input("Enter the Glucose value: "))
c = int(input("Enter the Blood Pressure Level: "))
d = int(input("Enter the Skin Thickness: "))
e = int(input("Enter the Insulin level: "))
f = float(input("Enter BMI: "))
g = float(input("Enter the Diabetes Pedigree Function: "))
h = int(input("Enter the age: "))

input_data = (a,b,c,d,e,f,g,h)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)
if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')