#requirements.txt 필요
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go

insurance_data = pd.read_csv("./insurance.csv")
insurance_data['bmi'] = insurance_data['bmi'].apply(round) #시각화 편의상 BMI를 round

def df_insure_data():     
    return insurance_data

### 각 지역별로 데이터 나누기 
def df_southwest_data():
    southwest_data = insurance_data.query("region == 'southwest'")
    return southwest_data

def df_northwest_data():
    northwest_data = insurance_data.query("region == 'northwest'")
    return northwest_data

def df_southeast_data():
    southeast_data = insurance_data.query("region == 'southeast'")
    return southeast_data

def df_northeast_data():
    northeast_data = insurance_data.query("region == 'northeast'")
    return northeast_data

