#requirements.txt 필요

#from tkinter import W
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import scipy

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, LabelEncoder
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.ensemble import RandomForestRegressor

import data as df
import age 
import bmi
import smoker 
import observation
import predict_charges as pred
import base64

st.set_page_config(layout= "wide")

#############DISPLAY#################
def intro():
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
    add_bg_from_local('insurance_image_edit.jpg')    

    st.title("EDA on Medical Cost in the beneficiary's residential area in the US")
    st.sidebar.success("Select a menu")
    
    st.write("made by bandi12424@naver.com") 
    st.write("dataset: https://www.kaggle.com/datasets/mirichoi0218/insurance ")
    st.markdown('#### Data description:')
    st.markdown("###### - age: age of primary beneficiary")
    st.markdown("###### - sex: insurance contractor gender, female, male")
    st.markdown("###### - bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight using the ratio of height to weight, ideally 18.5 to 24.9")
    st.markdown("###### - children: Number of children covered by health insurance / Number of dependents")
    st.markdown("###### - smoker: Smoking")
    st.markdown("###### - region: the beneficiary residential area in the US, northeast, southeast, southwest, northwest")
    st.markdown("###### - charges: Individual medical costs billed by health insurance")


def data_anal():
    age_tab, smoking_tab, bmi_tab = st.tabs(["Age", "Smoking", "BMI"] ) #max tab 갯수 = 3
    
    with age_tab: ###나이 
        st.write("Please explore this page in full screen :D")
        
        d_col29, d_col30 = st.columns(2)
        with d_col29: 
            st.plotly_chart(age.age_distribution_fig)
        with d_col30:
            st.plotly_chart(age.group_avg_bar_fig)
        
        st.header("Charges in each region depending on age")
        #display
        d_col21, d_col22 = st.columns(2)
        with d_col21:
            st.plotly_chart(age.SW_charge_age_fig)
        with d_col22:
            st.plotly_chart(age.SE_charge_age_fig)    
            
        d_col23, d_col24 = st.columns(2)
        with d_col23:
            st.plotly_chart(age.NW_charge_age_fig)
        with d_col24:
            st.plotly_chart(age.NE_charge_age_fig)    
        
        st.subheader("Charges in each region depending on gender and age")
        d_col5, d_col6 = st.columns(2)
        with d_col5:
            st.plotly_chart(age.SW_charge_age_fig_MF)
        with d_col6:
            st.plotly_chart(age.SE_charge_age_fig_MF)

        d_col7, d_col8 = st.columns(2)
        with d_col7:
            st.plotly_chart(age.NW_charge_age_fig_MF)
        with d_col8:
            st.plotly_chart(age.NE_charge_age_fig_MF)

        #bar_Chart 
        st.subheader("Average number of children for each generation")
        d_col1, d_col2 = st.columns(2)
        with d_col1:
            st.plotly_chart(age.SW_charge_age_bar_fig_MF)
        with d_col2:
            st.plotly_chart(age.SE_charge_age_bar_fig_MF)
            
        d_col3, d_col4 = st.columns(2)
        with d_col3:
            st.plotly_chart(age.NW_charge_age_bar_fig_MF)
        with d_col4:
            st.plotly_chart(age.NE_charge_age_bar_fig_MF)

    with smoking_tab: 
        st.write("Please explore this page in full screen :D")
        st.subheader("Smoking ratio in each region ")
        d_col17, d_col18 = st.columns(2)
        with d_col17:
            st.plotly_chart(smoker.SW_sunburst_fig)
        with d_col18:
            st.plotly_chart(smoker.SE_sunburst_fig)

        d_col19, d_col20 = st.columns(2)
        with d_col19:
            st.plotly_chart(smoker.NW_sunburst_fig)
        with d_col20:
            st.plotly_chart(smoker.NE_sunburst_fig)
            
        #display
        st.subheader("Charges in each region: smoker vs non-smoker")
        d_col9, d_col10 = st.columns(2)
        with d_col9:
            st.plotly_chart(smoker.SW_charge_age_fig_SM)
        with d_col10:
            st.plotly_chart(smoker.SE_charge_age_fig_SM)    

        d_col11, d_col12 = st.columns(2)
        with d_col11:
            st.plotly_chart(smoker.NW_charge_age_fig_SM)
        with d_col12:
            st.plotly_chart(smoker.NE_charge_age_fig_SM)

        st.subheader("BMI and charges of smokers in each region")
        d_col13, d_col14 = st.columns(2)
        with d_col13:
            st.plotly_chart(smoker.SW_charge_age_bar_fig_smo)
        with d_col14:
            st.plotly_chart(smoker.SE_charge_age_bar_fig_smo)

        d_col15, d_col16 = st.columns(2)
        with d_col15:
            st.plotly_chart(smoker.NW_charge_age_bar_fig_smo)
        with d_col16:
            st.plotly_chart(smoker.NE_charge_age_bar_fig_smo)
        
        st.subheader("BMI and charges of non-smokers in each region")
        d_col25, d_col26 = st.columns(2)
        with d_col25:
            st.plotly_chart(smoker.SW_charge_age_bar_fig_smo)
        with d_col26:
            st.plotly_chart(smoker.SE_charge_age_bar_fig_smo)

        d_col27, d_col28 = st.columns(2)
        with d_col27:
            st.plotly_chart(smoker.NW_charge_age_bar_fig_smo)
        with d_col28:
            st.plotly_chart(smoker.NE_charge_age_bar_fig_smo)
            
    with bmi_tab: #BMI 고려 
        st.write("Please explore this page in full screen :D")
        st.table(bmi.criterion)
        st.plotly_chart(bmi.bmi_group_avg_bar_fig)
        
        st.subheader("Average charges in each BMI group")
        d_col29, d_col30 = st.columns(2)
        with d_col29:
            st.plotly_chart(bmi.bmi_low_data_avg_bar_fig)
        with d_col30:
            st.plotly_chart(bmi.bmi_nor_data_avg_bar_fig)

        d_col31, d_col32 = st.columns(2)
        with d_col31:
            st.plotly_chart(bmi.bmi_over_data_avg_bar_fig)
        with d_col32:
            st.plotly_chart(bmi.bmi_obe_data_avg_bar_fig)
            
        
def average():
    #지역과 나이, 성별, 흡연여부를 입력했을 때, charges의 평균을 구하도록 해보자 
    st.header("Averages on charges")

    age = st.number_input("Age", min_value = 1, step = 1, format = "%d")
    region = st.selectbox("Region", options = ['southwest', 'southeast', 'northwest', 'northeast'])
    sex = st.radio("Sex", options = ['female', 'male'])
    smoking = st.radio("Smoker", options = ['yes', 'no'])
    insurance_data = df.df_insure_data()
    
    if st.button("submit"): #버튼이 눌리면
        #해당하는 data의 average 계산
        op_region = (insurance_data['region'] == region)
        op_age = (insurance_data['age'] == age)
        op_sex = (insurance_data['sex'] == sex)
        op_smoking = (insurance_data['smoker'] == smoking)

        result = insurance_data[op_region & op_age & op_sex & op_smoking]
        avg = round(result['charges'].mean(),2)
            
        if len(result) == 0: #해당하는 데이터가 없음
            st.write("There is no such data. Please choose another value")
        else:
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Age", value = age)
            col2.metric("Region", value = region)
            col3.metric("Sex", value = sex)
            col4.metric("Smoker", value = smoking)
                    
            st.subheader(f"Average charge: {avg} $")
            st.write("selected dataset")
            st.dataframe(result)
    else:
        st.write("Press the sumbit button")

def observe():
    st.header("Observation")
    
    with st.expander("Which generation has the highest charges?"):
        observation.high_generation()
    
    with st.expander("Which region has the highest average charges?"):
        st.write("Southeast region")
        st.plotly_chart(observation.region_avg_bar_fig)
        
    with st.expander("which BMI group has the highest average charges?"):
        observation.high_bmi()
        
    with st.expander("Person with the highest charges in each region"):
        observation.high_charge_in_region()
        
    with st.expander("Person with the lowest charges in each region"):
        observation.low_charge_in_region()
        
    with st.expander("Correlation of Features"):
        observation.draw_heatmap()
    
def predict_charges():
    #나이, bmi, 자식 수, 성별, 흡연여부, 지역을 입력했을 때, 예상 charges를 구해본다. 
    st.header("Expecting charges")
    
    #데이터 로드 및 모델 생성 
    insurance_data = df.df_insure_data()
    model = pred.training_process(pred.data_preprocessing(insurance_data.drop('generation', axis = 1)))

    input_age = st.number_input("Age", min_value = 1, step = 1, format = "%d")
    input_bmi = st.number_input("BMI", min_value = 1, step = 1, format = "%d")
    input_numOfChild = st.selectbox("Number of children", options = [i for i in range(10)])
    input_sex = st.radio("Sex", options = ['female', 'male'])
    input_smoking = st.radio("Smoker", options = ['yes', 'no'])
    input_region = st.radio("Region", options = ['southwest', 'southeast', 'northwest', 'northeast'])
    
    if st.button("submit"): #버튼이 눌리면
        #입력 여부 체크
        if input_age < 14 and input_numOfChild > 0:
            st.write("Check your input again (in particular, number of children)")
        else:    
            #예측을 위해 형변환
            region_list = ['northeast', 'northwest', 'southeast', 'southwest']
            input_sex = 1 if input_sex == 'female' else 2
            input_smoking = 1 if input_smoking == 'yes' else 0 
            input_region = region_list.index(input_region)

            result = pred.predict_cost(model, [input_age, input_bmi, input_numOfChild, input_sex, input_smoking, input_region])
            
            st.subheader(f"Prediction result: {result[0]:.2f}$")
    else:
        st.write("Press the sumbit button")
        
            
page_names_to_funcs = {
    "Intro": intro,
    "Data Visualization": data_anal,
    "Compute average charge": average,
    "Observation": observe,
    "Expecting charges": predict_charges
}

demo_name = st.sidebar.selectbox("Choose", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
