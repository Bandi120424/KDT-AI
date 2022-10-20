#requirements.txt 필요
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go

#https://bandi120424-ai-dev-course-month1-projectapp-month-1-vxuiyx.streamlitapp.com/

st.set_page_config(layout= "wide")
insurance_data = pd.read_csv("Month1_project/insurance.csv")

### 각 지역별로 데이터 나누기 
southwest_data = insurance_data.query("region == 'southwest'")
northwest_data = insurance_data.query("region == 'northwest'")
southeast_data = insurance_data.query("region == 'southeast'")
northeast_data = insurance_data.query("region == 'northeast'")

#########지역별 age & sex 기준 plot#################
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
SW_charge_age_bar_fig_MF = px.bar(southwest_data, x = 'age', y='charges', facet_col = 'sex')
SW_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Southwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SW_charge_age_fig_MF.update_xaxes(autorange=True)
SW_charge_age_fig_MF.update_yaxes(autorange=True)

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
SE_charge_age_bar_fig_MF = px.bar(southeast_data, x = 'age', y='charges', facet_col = 'sex')
SE_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Southeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SE_charge_age_fig_MF.update_xaxes(autorange=True)
SE_charge_age_fig_MF.update_yaxes(autorange=True)

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
NW_charge_age_bar_fig_MF = px.bar(northwest_data, x = 'age', y='charges', facet_col = 'sex')
NW_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Northwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NW_charge_age_fig_MF.update_xaxes(autorange=True)
NW_charge_age_fig_MF.update_yaxes(autorange=True)

#scatter plot
NE_charge_age_fig_MF = px.scatter(northeast_data, x = 'age', y='charges', color = 'sex')
NE_charge_age_fig_MF.update_layout(
    title={
        'text': "Northwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NE_charge_age_fig_MF.update_xaxes(autorange=True)
NE_charge_age_fig_MF.update_yaxes(autorange=True, tickprefix="$")

#bar plot
NE_charge_age_bar_fig_MF = px.bar(northeast_data, x = 'age', y='charges', facet_col = 'sex')
NE_charge_age_bar_fig_MF.update_layout(
    title={
        'text': "Northwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NE_charge_age_fig_MF.update_xaxes(autorange=True)
NE_charge_age_fig_MF.update_yaxes(autorange=True)

############## 각 지역별 흡연여부, 성별 기준 plot ###########################
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
SW_charge_age_bar_fig_SM = px.bar(southwest_data, x = 'age', y='charges', facet_col = 'smoker')
SW_charge_age_bar_fig_SM.update_layout(
    title={
        'text': "Southwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SW_charge_age_fig_SM.update_xaxes(autorange=True)
SW_charge_age_fig_SM.update_yaxes(autorange=True)


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
SE_charge_age_bar_fig_SM = px.bar(southeast_data, x = 'age', y='charges', facet_col = 'smoker')
SE_charge_age_bar_fig_SM.update_layout(
    title={
        'text': "Southeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
SE_charge_age_fig_SM.update_xaxes(autorange=True)
SE_charge_age_fig_SM.update_yaxes(autorange=True)

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
NW_charge_age_bar_fig_SM = px.bar(northwest_data, x = 'age', y='charges', facet_col = 'smoker')
NW_charge_age_bar_fig_SM.update_layout(
    title={
        'text': "Northwest",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NW_charge_age_fig_SM.update_xaxes(autorange=True)
NW_charge_age_fig_SM.update_yaxes(autorange=True)


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
NE_charge_age_bar_fig_SM = px.bar(northeast_data, x = 'age', y='charges', facet_col = 'smoker')
NE_charge_age_bar_fig_SM.update_layout(
    title={
        'text': "Northeast",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)
NE_charge_age_fig_SM.update_xaxes(autorange=True)
NE_charge_age_fig_SM.update_yaxes(autorange=True)


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

#############DISPLAY#################
def intro():
    st.title("EDA on Medical Cost in the beneficiary's residential area in the US")
    st.sidebar.success("Select a menu")
    
    st.write("made by bandi12424@naver.com") 
    st.write("dataset: https://www.kaggle.com/datasets/mirichoi0218/insurance ")
    st.write("Data description:")
    st.write("- age: age of primary beneficiary")
    st.write("- sex: insurance contractor gender, female, male")
    st.write("- bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight using the ratio of height to weight, ideally 18.5 to 24.9")
    st.write("- children: Number of children covered by health insurance / Number of dependents")
    st.write("- smoker: Smoking")
    st.write("- region: the beneficiary residential area in the US, northeast, southeast, southwest, northwest")
    st.write("- charges: Individual medical costs billed by health insurance")
        

def data_anal():
    tab1, tab2, tab3 = st.tabs(["age & sex", "age & smoking", "smoking ratio"] ) #max tab 갯수 = 3

    with tab1: ###나이별, 성별 요금 
        st.header("Charges: age & sex in each region ")
        #display
        d_col5, d_col6 = st.columns(2)
        with d_col5:
            st.plotly_chart(SW_charge_age_fig_MF)
        with d_col6:
            st.plotly_chart(SE_charge_age_fig_MF)

        d_col7, d_col8 = st.columns(2)
        with d_col7:
            st.plotly_chart(NW_charge_age_fig_MF)
        with d_col8:
            st.plotly_chart(NE_charge_age_fig_MF)

        d_col1, d_col2 = st.columns(2)
        with d_col1:
            st.plotly_chart(SW_charge_age_bar_fig_MF)
        with d_col2:
            st.plotly_chart(SE_charge_age_bar_fig_MF)
            
        d_col3, d_col4 = st.columns(2)
        with d_col3:
            st.plotly_chart(NW_charge_age_bar_fig_MF)
        with d_col4:
            st.plotly_chart(NE_charge_age_bar_fig_MF)

    with tab2: 
        st.header("Charges: age & smoking in each region ")
        #display
        d_col9, d_col10 = st.columns(2)
        with d_col9:
            st.plotly_chart(SW_charge_age_fig_SM)
        with d_col10:
            st.plotly_chart(SE_charge_age_fig_SM)    

        d_col11, d_col12 = st.columns(2)
        with d_col11:
            st.plotly_chart(NW_charge_age_fig_SM)
        with d_col12:
            st.plotly_chart(NE_charge_age_fig_SM)

        d_col13, d_col14 = st.columns(2)
        with d_col13:
            st.plotly_chart(SW_charge_age_bar_fig_SM)
        with d_col14:
            st.plotly_chart(SE_charge_age_bar_fig_SM)

        d_col15, d_col16 = st.columns(2)
        with d_col15:
            st.plotly_chart(NW_charge_age_bar_fig_SM)
        with d_col16:
            st.plotly_chart(NE_charge_age_bar_fig_SM)
        
    with tab3: #smoking ratio
        st.header("smoking ratio in each region ")
        d_col17, d_col18 = st.columns(2)
        with d_col17:
            st.plotly_chart(SW_sunburst_fig)
        with d_col18:
            st.plotly_chart(SE_sunburst_fig)

        d_col19, d_col20 = st.columns(2)
        with d_col19:
            st.plotly_chart(NW_sunburst_fig)
        with d_col20:
            st.plotly_chart(NE_sunburst_fig)

    # tab4, tab5, tab6 = st.tabs(["BMI & age", "BMI & smoking", "bmi & sex"] ) #max tab 갯수 = 3
    # with tab4:
    #     st.header("Charges: BMI & age in each region ")
    # with tab5:
    #     st.header("Charges: BMI & smoking in each region ")
    # with tab6:
    #     st.header("Charges: bmi & sex in each region ")
    
    
def average():
    #지역과 나이, 성별, 흡연여부를 입력했을 때, charges의 평균을 구하도록 해보자 
    st.header("Averages on charges")

    age = st.number_input("age", min_value = 1, step = 1, format = "%d")
    region = st.selectbox("region", options = ['southwest', 'southeast', 'northwest', 'northeast'])
    sex = st.radio("sex", options = ['female', 'male'])
    smoking = st.radio("smoker", options = ['yes', 'no'])

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

page_names_to_funcs = {
    "Intro": intro,
    "Data Analysis": data_anal,
    "Average": average
}

demo_name = st.sidebar.selectbox("Choose", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
