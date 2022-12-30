#requirements.txt 필요
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns 

import data as df
import age
import bmi

insurance_data = df.df_insure_data()

southwest_data = df.df_southwest_data()
southeast_data = df.df_southeast_data()
northwest_data = df.df_northwest_data()
northeast_data = df.df_northeast_data()
    
sw_avg = southwest_data['charges'].mean()
se_avg = southeast_data['charges'].mean()
nw_avg = northwest_data['charges'].mean()
ne_avg = northeast_data['charges'].mean()

#region별 평균 
val_y = [sw_avg, se_avg, nw_avg, ne_avg]
val_x = ['Southwest', 'Southeast', 'Northwest', 'Northeast']
region_avg_bar_fig = px.bar(x = val_x, y =val_y, color = val_x)

#각 지역에서 가장 높은 charge를 가진 사람의 정보
def high_charge_in_region():
    op1 = southwest_data['charges'] == max(southwest_data['charges'])
    st.dataframe(southwest_data[op1])
    
    op2 = southeast_data['charges'] == max(southeast_data['charges'])
    st.dataframe(southeast_data[op2])
    
    op3 = northwest_data['charges'] == max(northwest_data['charges'])
    st.dataframe(northwest_data[op3])
    
    op4 = northeast_data['charges'] == max(northeast_data['charges'])
    st.dataframe(northeast_data[op4])


def low_charge_in_region(): #각 지역에서 가장 낮은 charge를 가진 사람의 정보
    op1 = southwest_data['charges'] == min(southwest_data['charges'])
    st.dataframe(southwest_data[op1])
    
    op2 = southeast_data['charges'] == min(southeast_data['charges'])
    st.dataframe(southeast_data[op2])
    
    op3 = northwest_data['charges'] == min(northwest_data['charges'])
    st.dataframe(northwest_data[op3])
    
    op4 = northeast_data['charges'] == min(northeast_data['charges'])
    st.dataframe(northeast_data[op4])

def high_generation():
    st.write("sixties")
    st.write("In fact, it is likely to increase by age.")

    st.plotly_chart(age.group_avg_bar_fig)
    
def high_bmi():
    st.write("obesity group")
    st.write("In fact, it is likely to increase by BMI.")

    st.plotly_chart(bmi.bmi_group_avg_bar_fig)

def draw_heatmap():
    corr_data = insurance_data.corr()
    colormap = plt.cm.PuBu
    fig, ax = plt.subplots(figsize = (8,6))
    st.write("We can see that age is the most related numerical features to charges (our target feature!) and BMI is the next.")
    plt.title('Correlation between numerical features', y = 1, size = 10)
    sns.heatmap(corr_data, vmax = 8, linewidths = 0.1, square = True, annot = True, cmap = colormap, linecolor = 'white', annot_kws = {'size': 10})
    st.write(fig)
