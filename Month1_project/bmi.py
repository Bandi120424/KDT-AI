#requirements.txt 필요
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go

import data as df

southwest_data = df.df_southwest_data()
southeast_data = df.df_southeast_data()
northwest_data = df.df_northwest_data()
northeast_data = df.df_northeast_data()

insurance_data = df.df_insure_data()

#저제중, 정상체중, 과제충, 비만 기분으로 데이터 나눔 
bmi_low = (0<= insurance_data['bmi']) & (insurance_data['bmi'] < 20)
bmi_normal = (20<= insurance_data['bmi']) & (insurance_data['bmi'] < 25)
bmi_over = (25 <= insurance_data['bmi']) & (insurance_data['bmi'] < 30)
bmi_obe = (30<= insurance_data['bmi'])

bmi_low_df = insurance_data[bmi_low]
bmi_nor_df = insurance_data[bmi_normal]
bmi_over_df = insurance_data[bmi_over]
bmi_obe_df = insurance_data[bmi_obe]

#group별 BMI 평균 
val_y = [bmi_low_df['charges'].mean(),  bmi_nor_df['charges'].mean(), bmi_over_df['charges'].mean(), bmi_obe_df['charges'].mean()]
val_x = ['0 - 19', '20 - 24', '25 - 29', 'over 30']
bmi_group_avg_bar_fig = px.bar(x = val_x, y =val_y)
bmi_group_avg_bar_fig.update_layout(
    title={
        'text': 'x: BMI, y: charges',
        'y':0.825,
        'x':0.15,
        'xanchor': 'left',
        'yanchor': 'top'}
)

#각 group에서 BMI에 따른 평균 charge 
bmi_low_data_avg = bmi_low_df .groupby('bmi').mean()
bmi_low_data_avg_bar_fig = px.bar(bmi_low_data_avg, y = 'charges')
bmi_low_data_avg_bar_fig.update_layout(
    title={
        'text': "Low BMI",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

bmi_nor_data_avg = bmi_nor_df .groupby('bmi').mean()
bmi_nor_data_avg_bar_fig = px.bar(bmi_nor_data_avg, y = 'charges')
bmi_nor_data_avg_bar_fig.update_layout(
    title={
        'text': "Normal BMI",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

bmi_over_data_avg = bmi_low_df .groupby('bmi').mean()
bmi_over_data_avg_bar_fig = px.bar(bmi_over_data_avg, y = 'charges')
bmi_over_data_avg_bar_fig.update_layout(
    title={
        'text': "Overweight BMI",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

bmi_obe_data_avg = bmi_obe_df .groupby('bmi').mean()
bmi_obe_data_avg_bar_fig = px.bar(bmi_obe_data_avg, y = 'charges')
bmi_obe_data_avg_bar_fig.update_layout(
    title={
        'text': "Obesity BMI",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

