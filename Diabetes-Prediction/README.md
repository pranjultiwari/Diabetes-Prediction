# Diabetes-Prediction
# AIM:
To Predict whether the person is Diabetic or not.
# Diabetes:
Diabetes is a health condition that affects how your body turns food into energy. Most of the food you eat is broken down into sugar (also called glucose) and released into your bloodstream. When your blood sugar goes up, it signals your pancreas to release insulin.
Without ongoing, careful management, diabetes can lead to a build up of sugars in the blood, which can increase the risk of dangerous complications, including stroke and heart disease
# DATASET:
In this project i used <strong> Pima Indians Diabetes Database </strong> from Kaggle. This dataset is originally from the <strong> National Institute of Diabetes and Digestive and Kidney Diseases </strong> .
     I observed that there is no missing values in dataset however the features like Glucose, Blood Pressure, Insulin, Skin Thickness has 0 values which is not possible. We have to replace 0 values with either mean or median values of specific column.
# MODEL USED:
I tried different models and compare the accuracy for each. Then, I performed Hyperparameter Tuning on Models that has high accuracy. I have used Support Vector Machine Model for the prediction of Diabetes.

<h5>Here I have attached the preview image for explaining the identified hyperplane by Support vector machine (SVM) model.</h5>

![image](https://user-images.githubusercontent.com/113938735/201736405-429398f7-bb53-40f2-a52b-7052ed3dad79.png)

In the Support Vector Machine Model, as we train the Machine Learning Model with the Data the Support Vector Machine Model after training the data it identifies a hyperplane and divide it into Positive and Negative hyperplane.

<br>
<strong>Future scope </strong>
The diabetes prediction model can be made more creative by making an interactive user interface using flask to deploy this project on web, where the details of the parameters can be input by the user and an output will be reflected in a creative manner.
