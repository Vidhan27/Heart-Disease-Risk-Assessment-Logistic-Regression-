import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Load the pre-trained heart disease model
heart_model = pickle.load(open("heart_disease_model.sav", 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        'Heart Disease Risk Assessment',
        ['Prediction', 'Information', 'About Me', 'How To Use'],
        icons=['bag-plus'],
        default_index=0
    )

# Prediction section
if selected == 'Prediction':
    st.title("Heart Disease Risk Assessment")

    # Input fields for prediction

    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain Types')
    trestbps = st.text_input('Resting Blood Pressure')

    chol = st.text_input('Serum Cholesterol in mg/dl')

    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate Achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by fluoroscopy')

    thal = st.text_input('thal: 0 = normal ; 1 = fixed defect ; 2 = reversible defect')

    heart_diagnosis = ''

    # Prediction button
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has a chance of having heart disease'
        elif heart_prediction[0] == 0:
            heart_diagnosis = 'The person does not have a chance of heart disease'

        st.success(heart_diagnosis)

# Information Page
elif selected == 'Information':
    st.title('Information about Heart Disease')
    st.markdown(
        """
        <p style='font-size:25px;'>
        Heart disease is a broad term encompassing various conditions that affect the heart's structure and function, including coronary artery disease, heart attacks, and arrhythmias. Risk factors for heart disease include high blood pressure, high cholesterol, diabetes, smoking, obesity, and a sedentary lifestyle. Early warning signs may include chest pain or discomfort, shortness of breath, fatigue, or palpitations, but some individuals may have no symptoms until a serious event occurs. It is crucial to understand these risks and take preventive measures through a healthy diet, regular exercise, and routine medical check-ups. Prompt attention to any symptoms and proactive management can significantly reduce the risk of severe outcomes.
        </p>
        """, 
        unsafe_allow_html=True
    )

# About Me Page
elif selected == 'About Me':
    st.title('About Me')
    st.markdown(
        """
        <p style='font-size:25px;'>
        Me   Vidhan Prajapati   , A 3rd Year BTech Student pursuing  Computer Science at Karnavati University  <br>
        This project was made on purpose so that i can understand more about application of Machine Learning in healthcare , and would keep on learning
        Thanku for Vising
        </p>
        """, 
        unsafe_allow_html=True
    )

# How to Use Page
elif selected == 'How To Use':
    st.title('How to Use')
    st.markdown(
        """
        <p style='font-size:25px;'>
        This website is made to take in the inputs data of particular reading of a particular machine
        It would not be directly available to public
        But if you add the values it can make the prediction
        <br>This is just the demo of how prediction system would look like
        The algorithm used in model is Logistic Regression
        </p>
        """, 
        unsafe_allow_html=True
    )

