import streamlit as st
import pandas as pd
import numpy as np
import ML

st.markdown('# EDA AND PREDICTION FOR TITANIC DATASET')
gender = st.sidebar.selectbox(
    'Gender?',
    ('Male', 'Female')
)

ticket = st.sidebar.selectbox(
    'Ticket Classs?',
    ('1st = Upper Class',
    '2nd = Middle Class',
    '3rd = Lower Class')
)

age = st.sidebar.slider(
    'Age of the person',
    0,80
)

siblings = st.sidebar.slider(
    "Number of siblings",
    0,8
)

parch = st.sidebar.slider(
    "Number of parents/Children",
    0,6
)

fare = st.sidebar.text_input("Enter the fare")

embarked = st.sidebar.selectbox(
    "Port of Embarkation",
    ['Cherbourg', 'Queenstown', 'Southampton'])
