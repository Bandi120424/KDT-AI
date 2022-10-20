import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
#from plotly.subplots import make_subplots


insurance_data = pd.read_csv("./insurance.csv")

st.title("EDA on Medical Cost in the beneficiary's residential area in the US")

### 각 지역별로 데이터 나누기 
southwest_data = insurance_data.query("region == 'southwest'")
norhtwest_data = insurance_data.query("region == 'norhtwest'")
southeast_data = insurance_data.query("region == 'southeast'")
northeast_data = insurance_data.query("region == 'northeast'")

#fig = make_subplots(rows = 1, cols = 2) #streamlit에서는 지원하지 않는 듯 

###나이별, 성별 요금 
st.header("Charges: age & sex in each region ")
st.subheader("Southwest Region")
SW_charge_age_fig_MF = px.scatter(southwest_data, x = 'age', y='charges', color = 'sex')

SW_charge_age_fig_MF.update_xaxes(autorange=True)
SW_charge_age_fig_MF.update_yaxes(autorange=True, tickprefix="$")

st.plotly_chart(SW_charge_age_fig_MF)

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

st.plotly_chart(SW_charge_age_bar_fig_MF)

###흡연여부, 성별 요금 
st.header("Charges: smoker & sex in each region ")
st.subheader("Southwest Region")

SW_charge_age_fig_SM = px.scatter(southwest_data, x = 'age', y='charges', color = 'smoker')

SW_charge_age_fig_SM.update_xaxes(autorange=True)
SW_charge_age_fig_SM.update_yaxes(autorange=True, tickprefix="$")

st.plotly_chart(SW_charge_age_fig_SM)

SW_charge_age_bar_fig_SM = px.bar(southwest_data, x = 'age', y='charges', facet_col = 'smoker')
SW_charge_age_bar_fig_SM.update_layout(
    title={
        'text': "Southwest region charges per age",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SW_charge_age_fig_SM.update_xaxes(autorange=True)
SW_charge_age_fig_SM.update_yaxes(autorange=True)

st.plotly_chart(SW_charge_age_bar_fig_SM)

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

#4분할로 된 그래프를 만들고 싶음 
#fig.add_trace(charge_Age_SW_fig, row=1, col=1)
#fig.add_trace(charge_Age_SE_fig, row=1, col=2)


#(배포) streamlit은 streamlit cloud를 지원 

