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

def data_preprocessing(data): #범주형 -> 수치형 데이터로 변경 
    data['label_sex'] = (data['sex'] == 'male').astype(int) + 1
    data['label_smoker'] = (data['smoker'] == 'no').astype(int)
    
    le = LabelEncoder()
    le.fit(['northeast', 'northwest', 'southeast', 'southwest'])
    data['label_region'] = le.transform(data.region)
    
    return data
    
def training_process(data):
    
    X = data.drop(['charges', 'sex', 'smoker', 'region'], axis = 1)
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

    st.markdown("### Precision score of current regression model")
    st.write(f"[R2 Score] train data:{r2_score(y_train, forest_train_pred):.2f}%, test_data:{r2_score(y_test, forest_test_pred):.2f}%")
    saved_model = pickle.dumps(forest) #변수에 모델 저장
    #joblib.dump(forest, 'forest.pkl') #파일로 모델 저장 
    return saved_model
    

def predict_cost(pretrained_model, params): #성별, 나이, 지역, BMI, 흡연여부, 자식 수를 입력하면 예상치를 출력 
    #pretrained_model = joblib.load('forest.pkl') #파일로 저장한 모델을 사용할 경우 
    testdata = pd.DataFrame([{'age': params[0], 'bmi':params[1], 'children': params[2], 'label_sex': params[3], 'label_smoker': params[4], 'label_region':params[5]}], index = [0])
    
    poly_feats = PolynomialFeatures (degree = 2)
    X = poly_feats.fit_transform(testdata)
    model = pickle.loads(pretrained_model)
    
    return model.predict(X)
