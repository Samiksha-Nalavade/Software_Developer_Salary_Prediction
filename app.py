
# This file is called in the terminal to run the salary prediction app using streamlit to display in a web app.
import streamlit as st
st.set_page_config(page_title="Software Developer Salary Prediction", page_icon="📉", layout="wide", initial_sidebar_state="expanded", menu_items=None)




from PIL import Image
from predict_page import show_predict_page
from explore_page import show_explore_page

col1, col2, col3 = st.columns([3, 6, 1])
with col1:
    sru_logo = st.image(Image.open('xylogo.jpg'), use_column_width='auto', output_format='png')

with col2:
    pass

with col3:
    ai_logo = st.image(Image.open('SRU_AI_LOGO_digital_art_x4_colored_toned.jpg'), width=80, output_format='png')



image = Image.open('icon.png')
img = st.sidebar.image(image, width=30, use_column_width=80)
page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

about  = st.sidebar.markdown('''
## ABOUT
This is Machine Learning Web Application that helps in Predicting the Salary of a Software Developer based on their Experience, Location, Education Level, etc,\n

Web Application made with [Streamlit](https://streamlit.io/)  
Team:
- [Samiksha Nalavade]
- [Ruben Patel]
- [Arundhati Patil]
- [Prajakta Satpute]
- [Vaishnavi Katkar]
''')



sru_logo = st.sidebar.image(Image.open('xylogo.jpg'), use_column_width='auto', output_format='png')
if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
    