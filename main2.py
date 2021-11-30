import helper2  #importing all the helper fxn from helper.py which we will create later
import streamlit as st
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from datetime import datetime

st.set_page_config(layout='wide')
st.title('Logistics Planner')
st.image('sc_image.jpg')
st.subheader('Enter details of your shipment in the sidebar')


# Take Inputs
with st.form("my_form"):
    st.sidebar.header('Input Values')
    proj_code = st.sidebar.selectbox('1. Project Code', helper2.project)
    country = st.sidebar.selectbox('2. Destination Country', helper2.country)
    via = st.sidebar.selectbox('3. Fulfilled Via', helper2.via)
    inco = st.sidebar.selectbox('4. Inco Terms', helper2.inco)
    vendor = st.sidebar.selectbox('5. Vendor', helper2.vendor)
    manu_site = st.sidebar.selectbox('6. Manufacturing Site', helper2.manu_site)
    pq_date = st.sidebar.date_input('7. Price Quotation Date')
    po_date = st.sidebar.date_input('8. Purchase Order Date')
    sch_del_date = st.sidebar.date_input('9. Scheduled Delivery Date')
    line_value = st.sidebar.number_input('10. Value of Shipment (USD)')
    weight = st.sidebar.number_input('11. Weight (in kilograms)')
    insurance = st.sidebar.number_input('12. Insurance Value (USD)')
    submitted = st.form_submit_button('Get Prediction')
    if submitted:
        pq_date = pd.to_datetime(np.datetime64(pq_date))
        po_date = pd.to_datetime(np.datetime64(po_date))
        sch_del_date = pd.to_datetime(np.datetime64(sch_del_date))
        d = {'proj_code':proj_code,'country':country,'via':via,'inco':inco,'vendor':vendor,'line_value':line_value,
             'manu_site':manu_site, 'weight': weight,'insurance':insurance,'quote_date':pq_date,
             'po_date':po_date,'sch_del_date':sch_del_date}
        df = pd.DataFrame(data=d, index=[0])
        for column in helper2.date_columns:
            df[column + ' year'] = df[column].apply(lambda x: x.year)
            df[column + ' month'] = df[column].apply(lambda x: x.month)
            df[column + ' day'] = df[column].apply(lambda x: x.day)
        df = df.drop(helper2.date_columns, axis =1)
        df.columns = helper2.columns
        X = helper2.prep.transform(df)
        
        
        col1,col2,col3 = st.columns(3)
        mode_result = (helper2.mode_prediction(X)).upper()
        col1.header(f'{mode_result} TRANSPORT is the best mode for your cargo.')
        
        
        freight_result = (helper2.freight_prediction(X))
        col2.header(f'The expected freight cost is around USD {freight_result}.')
        
        delay_result = (helper2.delay_prediction(X))
        if delay_result > 0:
            col3.header(f'Your cargo might be delayed by {np.round(delay_result[0],0)} days.')
        else:
            col3.header(f'Your cargo might reach early by {delay_result*(-1)} days.')
            
        
        