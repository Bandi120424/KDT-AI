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

############## 각 지역별 흡연여부 기준 plot ###########################
#흡연여부는 성별보다 charge여부에 더 많은 영향을 미치는 듯함 

#지역별로 흡연자/비흡연자 데이터 나눔
southwest_smoker = southwest_data[southwest_data['smoker'] == 'yes']
southwest_non_smoker = southwest_data[southwest_data['smoker'] == 'no']
southwest_smoker_avg = southwest_smoker.groupby('age').mean() #나이별로 평균값 계산 
southwest_non_smoker_avg = southwest_non_smoker.groupby('age').mean()

southeast_smoker = southeast_data[southeast_data['smoker'] == 'yes']
southeast_non_smoker = southeast_data[southeast_data['smoker'] == 'no']
southeast_smoker_avg = southeast_smoker.groupby('age').mean()
southeast_non_smoker_avg = southeast_non_smoker.groupby('age').mean()

northwest_smoker = northwest_data[northwest_data['smoker'] == 'yes']
northwest_non_smoker = northwest_data[northwest_data['smoker'] == 'no']
northwest_smoker_avg = northwest_smoker.groupby('age').mean()
northwest_non_smoker_avg = northwest_non_smoker.groupby('age').mean()

northeast_smoker = northeast_data[northeast_data['smoker'] == 'yes']
northeast_non_smoker = northeast_data[northeast_data['smoker'] == 'no']
northeast_smoker_avg = northeast_smoker.groupby('age').mean()
northeast_non_smoker_avg = northeast_non_smoker.groupby('age').mean()


#scatter plot 
SW_charge_age_fig_SM = px.scatter(southwest_data, x = 'age', y='charges', color = 'smoker')
SW_charge_age_fig_SM.update_layout(
    title={
        'text': "Southwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SW_charge_age_fig_SM.update_xaxes(autorange=True)
SW_charge_age_fig_SM.update_yaxes(autorange=True, tickprefix="$")

#bar chart 
SW_charge_age_bar_fig_smo = px.bar(southwest_smoker_avg, y=['bmi', 'charges'])
SW_charge_age_bar_fig_smo.update_layout(
    title={
        'text': "Southwest smoker",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

#bar chart 
SW_charge_age_bar_fig_nsmo = px.bar(southwest_non_smoker_avg, y=['bmi', 'charges'])
SW_charge_age_bar_fig_nsmo.update_layout(
    title={
        'text': "Southwest non-smoker",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

#scatter plot 
SE_charge_age_fig_SM = px.scatter(southeast_data, x = 'age', y='charges', color = 'smoker')
SE_charge_age_fig_SM.update_layout(
    title={
        'text': "Southeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SE_charge_age_fig_SM.update_xaxes(autorange=True)
SE_charge_age_fig_SM.update_yaxes(autorange=True, tickprefix="$")

#bar chart 
SE_charge_age_bar_fig_smo = px.bar(southeast_smoker_avg, y=['bmi', 'charges'])
SE_charge_age_bar_fig_smo.update_layout(
    title={
        'text': "Southeast smoker",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

#bar chart 
SE_charge_age_bar_fig_nsmo = px.bar(southeast_non_smoker_avg, y=['bmi', 'charges'])
SE_charge_age_bar_fig_nsmo.update_layout(
    title={
        'text': "Southeast non-smoker",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)


#scatter plot 
NW_charge_age_fig_SM = px.scatter(northwest_data, x = 'age', y='charges', color = 'smoker')
NW_charge_age_fig_SM.update_layout(
    title={
        'text': "Northwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NW_charge_age_fig_SM.update_xaxes(autorange=True)
NW_charge_age_fig_SM.update_yaxes(autorange=True, tickprefix="$")

#bar chart 
NW_charge_age_bar_fig_smo = px.bar(northwest_smoker_avg, y=['bmi', 'charges'])
NW_charge_age_bar_fig_smo.update_layout(
    title={
        'text': "Northwest smoker",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

#bar chart 
NW_charge_age_bar_fig_nsmo = px.bar(northwest_non_smoker_avg, y=['bmi', 'charges'])
NW_charge_age_bar_fig_nsmo.update_layout(
    title={
        'text': "Northwest non-smoker",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

#scatter plot 
NE_charge_age_fig_SM = px.scatter(northeast_data, x = 'age', y='charges', color = 'smoker')
NE_charge_age_fig_SM.update_layout(
    title={
        'text': "Northeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NE_charge_age_fig_SM.update_xaxes(autorange=True)
NE_charge_age_fig_SM.update_yaxes(autorange=True, tickprefix="$")

#bar chart 
NE_charge_age_bar_fig_smo = px.bar(northeast_smoker_avg, y=['bmi', 'charges'])
NE_charge_age_bar_fig_smo.update_layout(
    title={
        'text': "Northeast smoker",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

#bar chart 
NE_charge_age_bar_fig_nsmo = px.bar(northeast_non_smoker_avg, y=['bmi', 'charges'])
NE_charge_age_bar_fig_nsmo.update_layout(
    title={
        'text': "Northeast non-smoker",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)


############ 지역별 나이-흡연여부-성별 순으로 sunburst chart##################
SW_sunburst_fig = px.sunburst(southwest_data, path=['smoker', 'sex'], values = 'charges', title = 'charges per smoker and sex')
colors=['#EF553B',
         '#636EFA']
criterion = ['smoker', 'non-smoker']

for i, m in enumerate(criterion):
    SW_sunburst_fig.add_annotation(dict(font=dict(color=colors[i],size=14),
                                        x=0.8,
                                        y=1-(i/10),
                                        showarrow=False,
                                        text=criterion[i],
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))

SW_sunburst_fig.update_layout(
     title={
        'text': "Southwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

SW_sunburst_fig.update_xaxes(tickfont=dict(color='rgba(0,0,0,0)'))
SW_sunburst_fig.update_yaxes(tickfont=dict(color='rgba(0,0,0,0)'))


SE_sunburst_fig = px.sunburst(southeast_data, path=['smoker', 'sex'], values = 'charges', title = 'charges per smoker and sex')
colors=['#EF553B',
         '#636EFA']
criterion = ['smoker', 'non-smoker']

for i, m in enumerate(criterion):
    SE_sunburst_fig.add_annotation(dict(font=dict(color=colors[i],size=14),
                                        x=0.8,
                                        y=1-(i/10),
                                        showarrow=False,
                                        text=criterion[i],
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))

SE_sunburst_fig.update_layout(
    title={
        'text': "Southeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

SE_sunburst_fig.update_xaxes(tickfont=dict(color='rgba(0,0,0,0)'))
SE_sunburst_fig.update_yaxes(tickfont=dict(color='rgba(0,0,0,0)'))


NW_sunburst_fig = px.sunburst(northwest_data, path=['smoker', 'sex'], values = 'charges', title = 'charges per smoker and sex')
colors=['#EF553B',
         '#636EFA']
criterion = ['smoker', 'non-smoker']

for i, m in enumerate(criterion):
    NW_sunburst_fig.add_annotation(dict(font=dict(color=colors[i],size=14),
                                        x=0.8,
                                        y=1-(i/10),
                                        showarrow=False,
                                        text=criterion[i],
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))

NW_sunburst_fig.update_layout(
     title={
        'text': "Northwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)


NW_sunburst_fig.update_xaxes(tickfont=dict(color='rgba(0,0,0,0)'))
NW_sunburst_fig.update_yaxes(tickfont=dict(color='rgba(0,0,0,0)'))


NE_sunburst_fig = px.sunburst(northeast_data, path=['smoker', 'sex'], values = 'charges', title = 'charges per smoker and sex')
colors=['#EF553B',
         '#636EFA']
criterion = ['smoker', 'non-smoker']

for i, m in enumerate(criterion):
    NE_sunburst_fig.add_annotation(dict(font=dict(color=colors[i],size=14),
                                        x=0.8,
                                        y=1-(i/10),
                                        showarrow=False,
                                        text=criterion[i],
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))

NE_sunburst_fig.update_layout(
    title={
        'text': "Northeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

NE_sunburst_fig.update_xaxes(tickfont=dict(color='rgba(0,0,0,0)'))
NE_sunburst_fig.update_yaxes(tickfont=dict(color='rgba(0,0,0,0)'))

