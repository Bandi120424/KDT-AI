#requirements.txt 필요
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns 
import scipy #plotly.figure_factory 사용을 위해 import
import matplotlib.pyplot as plt 
import plotly.express as px 
import plotly.graph_objects as go
import plotly.figure_factory as ff
 
import data as df

insurance_data = df.df_insure_data() 

southwest_data = df.df_southwest_data()
southeast_data = df.df_southeast_data()
northwest_data = df.df_northwest_data()
northeast_data = df.df_northeast_data()

#연령대 분포 
#avg_name = ["10", "twenties", "thirties", "forties", "fifties", "sixties"]

age_distribution_fig = px.histogram(insurance_data, x = 'generation', marginal="box")
age_distribution_fig.update_layout(
    title={
        'text': 'Age Distribution',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    autosize = True
)

#연령대별 평균정보를 구해보자
charge_avg_age = insurance_data.groupby('generation')['charges'].mean()

group_avg_bar_fig = px.bar(x = charge_avg_age.index, y = charge_avg_age, color = charge_avg_age.index)
group_avg_bar_fig.update_layout(
    title={
        'text': 'Average charges by generation',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title = 'generation',
    yaxis_title = 'average charges',
    showlegend=False,
    autosize = True
)

#########지역별 age plot#################
##성별 구분하지 않음 
#scatter plot
SW_charge_age_fig = px.scatter(southwest_data, x = 'age', y='charges', color = 'charges')
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
SE_charge_age_fig= px.scatter(southeast_data, x = 'age', y='charges', color = 'charges')
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
NW_charge_age_fig = px.scatter(northwest_data, x = 'age', y='charges', color = 'charges')
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
NE_charge_age_fig = px.scatter(northeast_data, x = 'age', y='charges', color = 'charges')
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
temp_colors = ['lightslategray'] * 6
temp_colors[2] = temp_colors[3] = 'crimson'

southwest_data_avg = southwest_data.groupby('generation').mean()
SW_charge_age_bar_fig_MF = go.Figure(data = [go.Bar (x = southwest_data_avg.index, y = southwest_data_avg['children'], marker_color=temp_colors)])
SW_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Southwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)


#bar plot
southeast_data_avg = southeast_data.groupby('generation').mean()
SE_charge_age_bar_fig_MF = go.Figure(data = [go.Bar (x = southeast_data_avg.index, y = southeast_data_avg['children'], marker_color=temp_colors)])
SE_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Southeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

#bar plot
northwest_data_avg = northwest_data.groupby('generation').mean()
NW_charge_age_bar_fig_MF = go.Figure(data = [go.Bar (x = northwest_data_avg.index, y = northwest_data_avg['children'], marker_color=temp_colors)])
NW_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Northwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

#bar plot
northeast_data_avg = northeast_data.groupby('generation').mean()
NE_charge_age_bar_fig_MF = go.Figure(data = [go.Bar (x = northeast_data_avg.index, y = northeast_data_avg['children'], marker_color=temp_colors)])
NE_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Northeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)



