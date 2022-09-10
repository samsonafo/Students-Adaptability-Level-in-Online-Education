#import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle

import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    layout='wide',
    page_title = 'Student Adaptabiliy Level in Online Learning',
    page_icon = 'img/icon.png',
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: shown;}
            footer {visibility: hidden;}
            footer:after {
                          content:'Created by Samson Afolabi'; 
                          visibility: visible;
                          display: block;
                          position: relative;
                          #background-color: white;
                          padding: 4px;
                          top: 2px;
                          }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#st.sidebar.image("img/side_img.jpg", width=250)

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
#set_background('')

st.title('Student Adaptibility Level in Online Learning')
image = Image.open('./img/header_img.jpg')
st.image(image, caption='Photo by David Marcu on Unsplash')


#load in pipeline
pipeline_file = './pipeline/gb_pipeline.pkl'
model = pickle.load(open(pipeline_file,'rb'))

#load in the y_label_encoder
y_enc_file = './pipeline/target_encoder.pkl'
y_enc = pickle.load(open(y_enc_file,'rb'))


def main():
    
    # get data and convert data into dataframe
    with st.form(key='my_form'):
        gender = st.selectbox('Gender',['male','female'])
        age = st.selectbox('Age',['6-10','11-15','16-20','21-25', '26-30'])
        education_level = st.selectbox('Education Level',['School', 'College','University'])
        institution_type = st.selectbox('Institution Type',['Non Government', 'Government'])
        it_student = st.selectbox('IT_Student',['Yes', 'No'])
        financial_condition = st.selectbox('Financial Condition',['Poor','Mid','Rich'])
        internet_type = st.selectbox('Internet Type',['Mobile Data', 'Wifi'])
        network_type = st.selectbox('Network Type',['2G','3G','4G'])
        class_duration = st.selectbox('Class Duration',['less than 1','1-3', '3-6'])
        device = st.selectbox('Device',['Mobile', 'Computer', 'Tab'])
        
        submit_button = st.form_submit_button(label='Submit')

    
    #define dataframe
    data_df = pd.DataFrame([[gender,age,education_level,institution_type,it_student,financial_condition,internet_type,network_type,class_duration,device]],
                               columns=['Gender', 'Age', 'Education Level', 'Institution Type','IT Student',
                                        'Financial Condition', 'Internet Type','Network Type','Class Duration','Device'])
    
    # predictions
    result = model.predict(data_df)
    
    #inverse_transform
    output = y_enc.inverse_transform(result)
    
    #calculate probability
    proba = model.predict_proba(data_df)
    probs = np.round(proba.max()*100,1)
    
    
    if submit_button:
        st.write('We predict your Adaptibility level to be',output[0],'with a probability of',probs)



main()


