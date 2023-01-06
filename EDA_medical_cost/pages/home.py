import streamlit as st
import base64

def home():
    add_bg_from_local('EDA_medical_cost/insurance_image_edit.jpg)    
    
    st.title("EDA on Medical Cost in the beneficiary's residential area in the US")
    st.sidebar.success("Select a menu")
    
    st.write("made by bandi12424@naver.com") 
    st.write("dataset: https://www.kaggle.com/datasets/mirichoi0218/insurance ")
    st.markdown(f"""
                #### Data description:
                - age: age of primary beneficiary
                - gender: insurance contractor gender, female, male
                - bmi: body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight using the ratio of height to weight
                - children: number of children covered by health insurance / number of dependents
                - smoker: smoker/non-smoker (yes/no)
                - region: the beneficiary residential area in the US, northeast, southeast, southwest, northwest
                - charges: individual medical costs billed by health insurance
                """ )

def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
            opacity:0.2
            background-size: cover;    
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    
    
    
