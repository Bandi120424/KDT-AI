import streamlit as st
import data as df

def average():
    #지역과 나이, 성별, 흡연여부를 입력했을 때, charges의 평균을 구하도록 해보자 
    st.header("Averages on charges")

    age = st.number_input("Age", min_value = 1, step = 1, format = "%d")
    region = st.selectbox("Region", options = ['southwest', 'southeast', 'northwest', 'northeast'])
    gender = st.radio("gender", options = ['female', 'male'])
    smoking = st.radio("Smoker", options = ['yes', 'no'])
    insurance_data = df.df_insure_data()
    
    if st.button("submit"): #버튼이 눌리면
        #해당하는 data의 average 계산
        op_region = (insurance_data['region'] == region)
        op_age = (insurance_data['age'] == age)
        op_gender = (insurance_data['gender'] == gender)
        op_smoking = (insurance_data['smoker'] == smoking)

        result = insurance_data[op_region & op_age & op_gender & op_smoking]
        avg = round(result['charges'].mean(),2)
            
        if len(result) == 0: #해당하는 데이터가 없음
            st.write("There is no such data. Please choose another value")
        else:
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Age", value = age)
            col2.metric("Region", value = region)
            col3.metric("gender", value = gender)
            col4.metric("Smoker", value = smoking)
                    
            st.subheader(f"Average charge: {avg} $")
            st.write("selected dataset")
            st.dataframe(result)
    else:
        st.write("Press the sumbit button")
