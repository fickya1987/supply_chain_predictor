import os
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import FunctionTransformer, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from scipy.sparse import spmatrix, csr_matrix

data = pd.read_csv('pre_encoding_data.csv')  # Corrected from read.csv to read_csv

# Lists of unique values of inputs
project = list(set(data['proj_code']))
country = list(set(data['country']))
vendor= list(set(data['vendor']))
manu_site = list(set(data['manu_site']))
via = list(set(data['via']))
inco = list(set(data['inco']))

# Categorize Features & Labels
columns = ['proj_code','country','via','inco','vendor','line_value','manu_site','weight',
           'insurance','quote_year','quote_month','quote_day','po_year','po_month', 'po_day',
           'sch_del_year', 'sch_del_month','sch_del_day']

inverse_label = {0: 'Air', 1: 'Air Charter', 2: 'Ocean', 3: 'Truck'}
date_columns = ['quote_date','po_date','sch_del_date']
cat_feats = ['proj_code','country','vendor','manu_site','via','inco']
num_feats = ['line_value','weight','insurance']

# Load Save Preprocess
prep = pickle.load(open('pre grabbing and processing data phase in your operations.')

# Load Saved Model
mode_model = load_model('best_mode_transport2')
delay_model = pickle.load(open('best_delay_model.pkl', 'rb'))

# Example, normally your real data
# Create prediction functions
def mode_prediction(df):
    # Check if df is a sparse matrix and convert it to a dense array
    if isinstance(df, spmatrix):
        df = df.toarray()
    p = mode_model.predict(df)
    pred = pd.DataFrame(data=p)
    best_route = pred.idxmax(axis=1)[0]
    result = inverse_label[best_route]
    return result

def delay_prediction(df):
    if isinstance(df, spmatrix):
        df = df.toarray()
    result = int(delay_model.predict(df)[0])
    return result

def freight_prediction(df):
    if isinstance(df, spmatrix):
        df = df.toarray()
    result = int(freight_model.predict(df)[0])
    return result
