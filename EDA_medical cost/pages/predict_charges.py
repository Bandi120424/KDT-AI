#for prediction
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, LabelEncoder
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

#for model save
import pickle
#from sklearn.externals import joblib

import data as df 
insurance_data = df.df_insure_data() 

def data_preprocessing(data): #범주형 -> 수치형 데이터로 변경 
    data['label_gender'] = (data['gender'] == 'male').astype(int) + 1
    data['label_smoker'] = (data['smoker'] == 'no').astype(int)
    
    le = LabelEncoder()
    le.fit(['northeast', 'northwest', 'southeast', 'southwest'])
    data['label_region'] = le.transform(data.region)
    
    return data
    
def training_process(data):
    
    X = data.drop(['charges', 'gender', 'smoker', 'region'], axis = 1)
    y = data.charges
    
    poly_feats = PolynomialFeatures (degree = 2)
    X_poly_feats = poly_feats.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_poly_feats, y, test_size=0.2, random_state = 42)
    
    forest = RandomForestRegressor(n_estimators = 100,
                              criterion = 'squared_error',
                              random_state = 42,
                              n_jobs = -1)
    
    forest.fit(X_train, y_train)

    forest_train_pred = forest.predict(X_train)
    forest_test_pred = forest.predict(X_test)

    st.markdown(f""" 
                     #### Current model description
                     - model: RandomForestRegressor
                     - preiction score: [R2 Score] train data:{r2_score(y_train, forest_train_pred):.2f}%, test_data:{r2_score(y_test, forest_test_pred):.2f}%                 
                """)

    saved_model = pickle.dumps(forest) #변수에 모델 저장
    #joblib.dump(forest, 'forest.pkl') #파일로 모델 저장 
    return saved_model
    

def predict_cost(pretrained_model, params): #성별, 나이, 지역, BMI, 흡연여부, 자식 수를 입력하면 예상치를 출력 
    #pretrained_model = joblib.load('forest.pkl') #파일로 저장한 모델을 사용할 경우 
    testdata = pd.DataFrame([{'age': params[0], 'bmi':params[1], 'children': params[2], 'label_gender': params[3], 'label_smoker': params[4], 'label_region':params[5]}], index = [0])
    
    poly_feats = PolynomialFeatures (degree = 2)
    X = poly_feats.fit_transform(testdata)
    model = pickle.loads(pretrained_model)
    
    return model.predict(X)

def predict_charges():
    #나이, bmi, 자식 수, 성별, 흡연여부, 지역을 입력했을 때, 예상 charges를 구해본다. 
    st.markdown(f""" 
                ## Expecting medical cost
                In this page, we can get an expecting medical cost with the following options. 
                """)
    
    #데이터 로드 및 모델 생성 
    insurance_data = df.df_insure_data()
    model = training_process(data_preprocessing(insurance_data.drop('generation', axis = 1)))

    input_age = st.number_input("Age", min_value = 1, step = 1, format = "%d")
    input_bmi = st.number_input("BMI", min_value = 1, step = 1, format = "%d")
    input_numOfChild = st.selectbox("Number of children", options = [i for i in range(10)])
    input_gender = st.radio("Gender", options = ['female', 'male'])
    input_smoking = st.radio("Smoker", options = ['yes', 'no'])
    input_region = st.radio("Region", options = ['southwest', 'southeast', 'northwest', 'northeast'])
    
    if st.button("submit"): #버튼이 눌리면
        #입력 여부 체크
        if input_age < 14 and input_numOfChild > 0:
            st.write("Check your input again (in particular, number of children)")
        else:    
            #예측을 위해 형변환
            region_list = ['northeast', 'northwest', 'southeast', 'southwest']
            input_gender = 1 if input_gender == 'female' else 2
            input_smoking = 1 if input_smoking == 'yes' else 0 
            input_region = region_list.index(input_region)

            result = predict_cost(model, [input_age, input_bmi, input_numOfChild, input_gender, input_smoking, input_region])
            
            st.subheader(f"Prediction result: {result[0]:.2f}$")
    else:
        st.write("Press the sumbit button")
        
