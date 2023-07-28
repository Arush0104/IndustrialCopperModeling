import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import statsmodels.api as sm
import numpy as np

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home","Regression Model","Classification Model"],
        icons = ["bi bi-house","binoculars","binoculars-fill"],
        menu_icon="cast",
        default_index=0
    )
def regression_model():
    st.markdown(" ## :blue[Kindly upload the excel file to get the predicted values of selling price]")
    uploadedfile=st.file_uploader('Choose an xlsx file', type='xlsx')
    if uploadedfile:
        df = pd.read_excel(uploadedfile,engine='openpyxl')
        label = "selling_price"
        y=df['selling_price']
        X=df[['quantity_tons','width','thickness']].assign(const=1)
        model = sm.OLS(y,X)
        results=model.fit()
        df['predicted_selling_price']=results.fittedvalues
        st.table(df)
        
        
#print(results.predict([put respective values here]))
def class_model():
    st.markdown(" ## :blue[Kindly upload the excel file to get the predicted values status]")
    st.markdown(" #### :orange[Note: Won is equivalent to 1 and 0 is equivalent to lost]")
    uploadedfiled=st.file_uploader('Choose an xlsx file', type='xlsx')
    if uploadedfiled:
        df1 = pd.read_excel(uploadedfiled,engine='openpyxl')
        df1['code']=pd.factorize(df1.status)[0]
        Y=df1['code']
        x=df1[['quantity_tons','width','thickness']].assign(const=1)
        model = sm.OLS(Y,x)
        results=model.fit()
        df1['Status_predicted']=results.fittedvalues
        df1['Status_predicted']= np.round(df1['Status_predicted'],decimals=0)
        st.table(df1[['quantity_tons','width','thickness','status','Status_predicted']])
        
if selected == "Home":
    st.markdown(" # :orange[Welcome to the home Page. Select an option to get started.]")
elif selected=="Regression Model":
    regression_model()
elif selected=="Classification Model":
    class_model()

    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
