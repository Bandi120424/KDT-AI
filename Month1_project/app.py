import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


insurance_data = pd.read_csv("insurance.csv")

st.title("EDA on Medical Cost in the beneficiary's residential area in the US")

### 각 지역별로 데이터 나누기 
southwest_data = insurance_data.query("region == 'southwest'")
northwest_data = insurance_data.query("region == 'northwest'")
southeast_data = insurance_data.query("region == 'southeast'")
northeast_data = insurance_data.query("region == 'northeast'")


###나이별, 성별 요금 
st.header("Charges: age & sex in each region ")
st.subheader("Southwest Region")
#scatter plot
SW_charge_age_fig_MF = px.scatter(southwest_data, x = 'age', y='charges', color = 'sex')

SW_charge_age_fig_MF.update_xaxes(autorange=True)
SW_charge_age_fig_MF.update_yaxes(autorange=True, tickprefix="$")

#bar chart 
SW_charge_age_bar_fig_MF = px.bar(southwest_data, x = 'age', y='charges', facet_col = 'sex')
SW_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Southwest region charges per age",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SW_charge_age_fig_MF.update_xaxes(autorange=True)
SW_charge_age_fig_MF.update_yaxes(autorange=True)

#display
st.plotly_chart(SW_charge_age_bar_fig_MF)
st.plotly_chart(SW_charge_age_fig_MF)


st.subheader("Southeast Region")
#scatter plot
SE_charge_age_fig_MF = px.scatter(southeast_data, x = 'age', y='charges', color = 'sex')

SE_charge_age_fig_MF.update_xaxes(autorange=True)
SE_charge_age_fig_MF.update_yaxes(autorange=True, tickprefix="$")

#bar plot
SE_charge_age_bar_fig_MF = px.bar(southeast_data, x = 'age', y='charges', facet_col = 'sex')
SE_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Southeast region charges per age",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SE_charge_age_fig_MF.update_xaxes(autorange=True)
SE_charge_age_fig_MF.update_yaxes(autorange=True)

st.plotly_chart(SE_charge_age_bar_fig_MF)
st.plotly_chart(SE_charge_age_fig_MF)

st.subheader("Northwest Region")
#scatter plot
NW_charge_age_fig_MF = px.scatter(northwest_data, x = 'age', y='charges', color = 'sex')

NW_charge_age_fig_MF.update_xaxes(autorange=True)
NW_charge_age_fig_MF.update_yaxes(autorange=True, tickprefix="$")

#bar plot
NW_charge_age_bar_fig_MF = px.bar(northwest_data, x = 'age', y='charges', facet_col = 'sex')
NW_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Northwest region charges per age",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NW_charge_age_fig_MF.update_xaxes(autorange=True)
NW_charge_age_fig_MF.update_yaxes(autorange=True)

st.plotly_chart(NW_charge_age_bar_fig_MF)
st.plotly_chart(NW_charge_age_fig_MF)

st.subheader("Northeast Region")
#scatter plot
NE_charge_age_fig_MF = px.scatter(northeast_data, x = 'age', y='charges', color = 'sex')

NE_charge_age_fig_MF.update_xaxes(autorange=True)
NE_charge_age_fig_MF.update_yaxes(autorange=True, tickprefix="$")

#bar plot
NE_charge_age_bar_fig_MF = px.bar(northeast_data, x = 'age', y='charges', facet_col = 'sex')
NE_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Northwest region charges per age",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NE_charge_age_fig_MF.update_xaxes(autorange=True)
NE_charge_age_fig_MF.update_yaxes(autorange=True)

st.plotly_chart(NE_charge_age_bar_fig_MF)
st.plotly_chart(NE_charge_age_fig_MF)


###흡연여부, 성별 요금 
st.header("Charges: smoker & sex in each region ")

st.subheader("Southwest Region")
#scatter plot 
SW_charge_age_fig_SM = px.scatter(southwest_data, x = 'age', y='charges', color = 'smoker')

SW_charge_age_fig_SM.update_xaxes(autorange=True)
SW_charge_age_fig_SM.update_yaxes(autorange=True, tickprefix="$")

#bar chart 
SW_charge_age_bar_fig_SM = px.bar(southwest_data, x = 'age', y='charges', facet_col = 'smoker')
SW_charge_age_bar_fig_SM.update_layout(
    title={
        'text': "Southwest region charges: age & smoking",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SW_charge_age_fig_SM.update_xaxes(autorange=True)
SW_charge_age_fig_SM.update_yaxes(autorange=True)

# 나이-흡연여부-성별 순으로 sunburst chart를 그려봅시다.
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
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

SW_sunburst_fig.update_xaxes(tickfont=dict(color='rgba(0,0,0,0)'))
SW_sunburst_fig.update_yaxes(tickfont=dict(color='rgba(0,0,0,0)'))

st.plotly_chart(SW_sunburst_fig)
st.plotly_chart(SW_charge_age_fig_SM)
st.plotly_chart(SW_charge_age_bar_fig_SM)


st.subheader("Southeast Region")
#scatter plot 
SE_charge_age_fig_SM = px.scatter(southeast_data, x = 'age', y='charges', color = 'smoker')

SE_charge_age_fig_SM.update_xaxes(autorange=True)
SE_charge_age_fig_SM.update_yaxes(autorange=True, tickprefix="$")

#bar chart 
SE_charge_age_bar_fig_SM = px.bar(southeast_data, x = 'age', y='charges', facet_col = 'smoker')
SE_charge_age_bar_fig_SM.update_layout(
    title={
        'text': "Southeast region charges: age & smoking",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SE_charge_age_fig_SM.update_xaxes(autorange=True)
SE_charge_age_fig_SM.update_yaxes(autorange=True)

# 나이-흡연여부-성별 순으로 sunburst chart를 그려봅시다.
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
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

SE_sunburst_fig.update_xaxes(tickfont=dict(color='rgba(0,0,0,0)'))
SE_sunburst_fig.update_yaxes(tickfont=dict(color='rgba(0,0,0,0)'))

st.plotly_chart(SE_sunburst_fig)
st.plotly_chart(SE_charge_age_fig_SM)
st.plotly_chart(SE_charge_age_bar_fig_SM)

st.subheader("Northwest Region")
#scatter plot 
NW_charge_age_fig_SM = px.scatter(northwest_data, x = 'age', y='charges', color = 'smoker')

NW_charge_age_fig_SM.update_xaxes(autorange=True)
NW_charge_age_fig_SM.update_yaxes(autorange=True, tickprefix="$")

#bar chart 
NW_charge_age_bar_fig_SM = px.bar(northwest_data, x = 'age', y='charges', facet_col = 'smoker')
NW_charge_age_bar_fig_SM.update_layout(
    title={
        'text': "Northwest region charges: age & smoking",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NW_charge_age_fig_SM.update_xaxes(autorange=True)
NW_charge_age_fig_SM.update_yaxes(autorange=True)

# 나이-흡연여부-성별 순으로 sunburst chart를 그려봅시다.
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
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

NW_sunburst_fig.update_xaxes(tickfont=dict(color='rgba(0,0,0,0)'))
NW_sunburst_fig.update_yaxes(tickfont=dict(color='rgba(0,0,0,0)'))

st.plotly_chart(NW_sunburst_fig)
st.plotly_chart(NW_charge_age_fig_SM)
st.plotly_chart(NW_charge_age_bar_fig_SM)


st.subheader("Northeast Region")
#scatter plot 
NE_charge_age_fig_SM = px.scatter(northeast_data, x = 'age', y='charges', color = 'smoker')

NE_charge_age_fig_SM.update_xaxes(autorange=True)
NE_charge_age_fig_SM.update_yaxes(autorange=True, tickprefix="$")

#bar chart 
NE_charge_age_bar_fig_SM = px.bar(northeast_data, x = 'age', y='charges', facet_col = 'smoker')
NE_charge_age_bar_fig_SM.update_layout(
    title={
        'text': "Northeast region charges: age & smoking",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NE_charge_age_fig_SM.update_xaxes(autorange=True)
NE_charge_age_fig_SM.update_yaxes(autorange=True)

# 나이-흡연여부-성별 순으로 sunburst chart를 그려봅시다.
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
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

NE_sunburst_fig.update_xaxes(tickfont=dict(color='rgba(0,0,0,0)'))
NE_sunburst_fig.update_yaxes(tickfont=dict(color='rgba(0,0,0,0)'))

st.plotly_chart(NE_sunburst_fig)
st.plotly_chart(NE_charge_age_fig_SM)
st.plotly_chart(NE_charge_age_bar_fig_SM)

