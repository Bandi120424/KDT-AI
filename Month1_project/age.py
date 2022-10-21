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

 #연령대별 평균정보를 구해보자
generation = [] #generation의 i번째 원소 = (i+1) 대 정보
for i in range(1, 7):
    generation.append(insurance_data[insurance_data['age']//10 == i])

charge_avg_age = [generation[i]['charges'].mean() for i in range(6)]
avg_name = ["teeanger", "twenties", "thirties", "forties", "fifties", "sixties"]

group_avg_bar_fig = px.bar(y = charge_avg_age, x = avg_name)
group_avg_bar_fig.update_layout(
    title={
        'text': 'Average charges by generation',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

#########지역별 age plot#################
#성별에 따라 
#scatter plot
SW_charge_age_fig_MF = px.scatter(southwest_data, x = 'age', y='charges', color = 'sex')
SW_charge_age_fig_MF.update_layout(
    title={
        'text': "Southwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SW_charge_age_fig_MF.update_xaxes(autorange=True)
SW_charge_age_fig_MF.update_yaxes(autorange=True, tickprefix="$")

#bar chart 
southwest_data_avg = southwest_data.groupby('age').mean()
SW_charge_age_bar_fig_MF = px.bar(southwest_data_avg, y = ['charges', 'bmi'])
SW_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Southwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

#scatter plot
SE_charge_age_fig_MF = px.scatter(southeast_data, x = 'age', y='charges', color = 'sex')
SE_charge_age_fig_MF.update_layout(
    title={
        'text': "Southeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SE_charge_age_fig_MF.update_xaxes(autorange=True)
SE_charge_age_fig_MF.update_yaxes(autorange=True, tickprefix="$")

#bar plot
southeast_data_avg = southeast_data.groupby('age').mean()
SE_charge_age_bar_fig_MF = px.bar(southeast_data_avg, y = ['charges', 'bmi'])
SE_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Southeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

#scatter plot
NW_charge_age_fig_MF = px.scatter(northwest_data, x = 'age', y='charges', color = 'sex')
NW_charge_age_fig_MF.update_layout(
    title={
        'text': "Northwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NW_charge_age_fig_MF.update_xaxes(autorange=True)
NW_charge_age_fig_MF.update_yaxes(autorange=True, tickprefix="$")

#bar plot
northwest_data_avg = northwest_data.groupby('age').mean()
NW_charge_age_bar_fig_MF = px.bar(northwest_data_avg, y = ['charges', 'bmi'])
NW_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Northwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

#scatter plot
NE_charge_age_fig_MF = px.scatter(northeast_data, x = 'age', y='charges', color = 'sex')
NE_charge_age_fig_MF.update_layout(
    title={
        'text': "Northeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NE_charge_age_fig_MF.update_xaxes(autorange=True)
NE_charge_age_fig_MF.update_yaxes(autorange=True, tickprefix="$")

#bar plot
northeast_data_avg = northeast_data.groupby('age').mean()
NE_charge_age_bar_fig_MF = px.bar(northeast_data_avg, y = ['charges', 'bmi'])
NE_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Northeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

##성별 구분하지 않음 
#scatter plot
SW_charge_age_fig = px.scatter(southwest_data, x = 'age', y='charges')
SW_charge_age_fig.update_layout(
    title={
        'text': "Southwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SW_charge_age_fig.update_xaxes(autorange=True)
SW_charge_age_fig.update_yaxes(autorange=True, tickprefix="$")

#scatter plot
SE_charge_age_fig= px.scatter(southeast_data, x = 'age', y='charges')
SE_charge_age_fig.update_layout(
    title={
        'text': "Southeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SE_charge_age_fig.update_xaxes(autorange=True)
SE_charge_age_fig.update_yaxes(autorange=True, tickprefix="$")

#scatter plot
NW_charge_age_fig = px.scatter(northwest_data, x = 'age', y='charges')
NW_charge_age_fig.update_layout(
    title={
        'text': "Northwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NW_charge_age_fig.update_xaxes(autorange=True)
NW_charge_age_fig.update_yaxes(autorange=True, tickprefix="$")

#scatter plot
NE_charge_age_fig = px.scatter(northeast_data, x = 'age', y='charges')
NE_charge_age_fig.update_layout(
    title={
        'text': "Northeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NE_charge_age_fig.update_xaxes(autorange=True)
NE_charge_age_fig.update_yaxes(autorange=True, tickprefix="$")

