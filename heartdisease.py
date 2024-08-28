import pickle
import streamlit as st
from streamlit_option_menu import option_menu

heart_model  = pickle.load(open("heart_disease_model.sav",'rb'))

with st.sidebar :
    selected = option_menu('Heart Disease Risk Assessment',['Prediction','Information','About Me','How To Use'],icons=['bag-plus'],default_index=0)

if selected == 'Prediction':
    st.title("Heart Disease Risk Assessment")

    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain Types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestrolm in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate Achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by fluoroscopy')
    thal = st.text_input('thal: 0 = normal ; 1 = fixed defect ; 2 = reversable defect')


    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):

        user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]

        user_input = [float(x) for x in user_input]

        heart_prediction  = heart_model.predict([user_input])

        if heart_prediction[0]==1:
            heart_diagnosis = 'The person has chance of having heart disease'
        elif heart_prediction[0]==0:
            heart_diagnosis='The person does not have a chance of heart disease'

        st.success(heart_diagnosis)
