#requirements.txt 필요
from tkinter import W
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go

#https://bandi120424-ai-dev-course-month1-projectapp-month-1-vxuiyx.streamlitapp.com/

import data as df
import age 
import bmi
import smoker 
import observation

st.set_page_config(layout= "wide")


#############DISPLAY#################
def intro():
    st.title("EDA on Medical Cost in the beneficiary's residential area in the US")
    st.sidebar.success("Select a menu")
    
    st.write("made by bandi12424@naver.com") 
    st.write("dataset: https://www.kaggle.com/datasets/mirichoi0218/insurance ")
    st.markdown('**Data description**:')
    st.write("- **age**: age of primary beneficiary")
    st.write("- **sex**: insurance contractor gender, female, male")
    st.write("- **bmi**: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight using the ratio of height to weight, ideally 18.5 to 24.9")
    st.write("- **children**: Number of children covered by health insurance / Number of dependents")
    st.write("- **smoker**: Smoking")
    st.write("- **region**: the beneficiary residential area in the US, northeast, southeast, southwest, northwest")
    st.write("- **charges**: Individual medical costs billed by health insurance")


def data_anal():
    tab1, tab2, tab3 = st.tabs(["Age", "Smoking", "BMI"] ) #max tab 갯수 = 3
    
    with tab1: ###나이 
        st.header("Charges in each region depending on age")
        st.write("Please explore this page in full screen :D")
        
        st.plotly_chart(age.group_avg_bar_fig)
        
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
        
        st.subheader("Let's consider a gender")
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
        st.subheader("Average charges, BMI, children for each age")
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

    with tab2: 
        st.header("Charges in each region depending on smoking")
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
        st.subheader("Charges in each region")
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

        st.subheader("Smoker in each region")
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
        
        st.subheader("Non-smoker in each region")
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
            
    with tab3: #BMI 고려 
        st.header("Charges depending on BMI")
        st.write("Please explore this page in full screen :D")
        
        st.plotly_chart(bmi.bmi_group_avg_bar_fig)
        
        st.subheader("Charges in each group depending on BMI")
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

    age = st.number_input("age", min_value = 1, step = 1, format = "%d")
    region = st.selectbox("region", options = ['southwest', 'southeast', 'northwest', 'northeast'])
    sex = st.radio("sex", options = ['female', 'male'])
    smoking = st.radio("smoker", options = ['yes', 'no'])
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
                    
            st.subheader(f"Average charge: {avg} dollar")
            st.write("selected dataset")
            st.dataframe(result)
    else:
        st.write("Press the sumbit button")

def observe():
    st.header("Observation about dataset")
    
    with st.expander("Which generation has the highest charges?"):
        observation.high_generation()
    
    with st.expander("Which region has the highest average charges?"):
        st.write("Southeast region")
        st.plotly_chart(observation.region_avg_bar_fig)
        
    with st.expander("which BMI group has the highest averga charges?"):
        observation.high_bmi()
        
    with st.expander("Person with the highest charges in each region"):
        observation.high_charge_in_region()
        
    with st.expander("Person with the lowest charges in each region"):
        observation.low_charge_in_region()
    
   
            
page_names_to_funcs = {
    "Intro": intro,
    "Data Visualization": data_anal,
    "Compute average charge": average,
    "Observation": observe
}

demo_name = st.sidebar.selectbox("Choose", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
