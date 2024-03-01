#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import streamlit as st
import numpy as np
from Prediction import predict


# In[8]:


import warnings
warnings.filterwarnings("ignore")


# In[9]:


st.title("Predict Mileage per Gallon")
st.markdown("Model to Predict MPG of a car")

st.header("Car Features")
col1, col2, col3, col4 = st.columns(4)
with col1 :
    cylinders = st.slider("cylinders", 2,8,1)
    displacement = st.slider("displacement", 50,500,10)
with col2:
    horsepower = st.slider("horsepower", 50,500,10)
    weight = st.slider("weight", 1500, 6000, 250)
with col3:
    acceleration = st.slider("acceleration", 8,25,1)
    modelyear = st.slider("modelyear", 70,85,1)
with col4:
    origin = st.slider("origin", 1,3,1)
    


# In[10]:


if st.button("Predict MPG of Car"):
    result = predict(np.array([[cylinders,displacement,horsepower,weight,acceleration,modelyear,origin]]))
    st.text(result[0])

