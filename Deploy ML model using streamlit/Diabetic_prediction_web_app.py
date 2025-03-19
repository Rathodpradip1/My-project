# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 22:29:25 2025

@author: HP
"""

import numpy as np # used to working with numpy array
import pickle  # used for 'wb' and 'rb'
import streamlit as st  # used for deployment

# loading the saved model
loaded_model = pickle.load(open("C:/Users/HP/Documents/trained_model.sav" , 'rb'))

# Creating a function for prediction

def diabetes_prediction(input_data):
    
    
   
    # Changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance 
    input_data_reshape = input_data_as_numpy_array.reshape(1 ,-1)

    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)

    if (prediction[0] == 0):
        return("The person is not diabetic")
    else:
        return("The person is diabetic")
    
# Now moving towards next part called streamlit part 

def main():
    
    
    # first step is giving the title 
    st.title("Diabetes Prediction Web App")    # title is the function within the streamlit library 
    
    # Next step is create input data field as user given all the values mentioned in the dataset
    # The user provided data sequence should be the same sequence as the data in the original dataset
    
    #getting input data from the user
    
    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure Value")
    SkinThickness = st.text_input("Skin Thikness value ")
    Insulin = st.text_input("Insulin Level ")
    BMI = st.text_input("BMI Level ")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction Value")
    Age = st.text_input("Age Of The Person")
    
    # Code for prediction
    diagnosis = ''
    
    # Creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies ,Glucose, BloodPressure,SkinThickness,Insulin, BMI ,DiabetesPedigreeFunction , Age])
        
    st.success(diagnosis)



if __name__ == '__main__':
    main()