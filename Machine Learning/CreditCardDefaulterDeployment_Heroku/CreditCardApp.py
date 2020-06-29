# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image


pickle_in = open("CreditCardClassifier (1).pkl","rb")
classifier=pickle.load(pickle_in)

def predict_credit_card_defaulter(Total_Credit,Age,Sex,Education, Marital_Status):
    Education = [0,0,0,0,0,1]
    Marital_Status = [0,0,1]
    """Let's validate bank defaulter 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Total_Credit
        in: query
        type: number
        required: true
      - name: Age
        in: query
        type: number
        required: true
      - name: Sex
        in: query
        type: number
        required: true
      - name: Education
        in: query
        type: number
        required: true
      - name: Education
        in: query
        type: number
        required: true
        
    responses:
        200:
            description: The output values
        
    """
    list1= [Total_Credit,Age,Sex,0,0,0,0,0,1,0,0,1,0,0]  
    # This needs to be reworked upon
    prediction=classifier.predict([list1])
    print(prediction)
    if prediction== 0:
        value = "Not Defaulter"
    elif prediction ==1: 
        value ="Defaulter"
    return value



def main():
    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Credit Card Fraud Detection ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Total_Credit = st.text_input("Total Credit","Type Here")
    Age = st.text_input("Age","Type Here")
    Sex = st.text_input("Sex (Type 1 for Male, Type 2 for Female)","Type Here")
    Education = st.text_input("Education (Type 1 if graduate, 2 if undergrad, 3 if high school)","Type Here")
    Marital_Status = st.text_input("Marital Status (Type 1 if married, 2 ifsingle)","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_credit_card_defaulter(Total_Credit,Sex,Education, Marital_Status, Age)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__== '__main__':
    main()
