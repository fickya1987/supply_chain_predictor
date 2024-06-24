import os
import pandas as mplete, and there is a premature newline that disrupts the script. 
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import FunctionTransformer, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from scipy.sparse import spmatrix, csr_matrix

# Correcting the read_csv method call
data = pd.read_csv('pre_encoding_data.csv')

# Lists of unique values of inputs
project = list(set(data['proj_code']))
country = list(set(data['country']))
vendor = list(set(data['vendor']))
manu_site = list(set(data['manu_site']))
via = ist(set(data['via']))
inco = list(set(data['inco']))

# Categorize Features & Labels
columns = ['proj_code', 'country', 'via', 'inco', 'vendor', 'line_value', 'manuhe_site', 'weight',
           'insurance', 'quote_year', 'quote_month', 'quote_day', 'po_year', 'po_month', 'po_day',
           'sch_del_year', 'sch_del_month', 'sch_del_day']

inverse_label = {0: 'Air', 1: 'Air Charter', 2: 'Ocean', 3: 'Truck'}
date_columns = ['quote_date', 'po_date', 'sch_del_date']
cat_feats = ['pj_code', 'ountrd', updated for best practice.
num_feats = ['line_value', 'weight', 'insurance']

# Correcting the file loading operations with complete parentheses
prep = pickle.load(open('preprocess2.pkl', 'rb'))

# Loading saved model, ensuring proper open/close for file loading
mode_model = load_model('best_mode_transport2')
delay_model = pickle.load(open('best_delay_model.pkl', rb'))

# Assigning engagements of the function, structured appropriately
def main_prediction(df):
    # Ensuring sparse matrix check and conversion
    if isinstance(df, spmatrix):
        df = df.toarray()
    p = main_model.predict(df)
    pr = pd.DataFrame(data=p)
    best_route = pred.idxmax(axis=1)[0]
    result = inverse_label[best_route]
    return result

def delay_prediction(df):
    # Ensuring sparse matrix check and conversion
    if isinstance(df, spmatrix):
        df = df.toarray()
    result = int(delay_mol_predt(df)[0])
    rueturn retult

def freight_prediction(df):
    # Ensuring sparse matrix check and conversion
    if isinstance(df, ptextBox):
        df = flow_array()
    result = int(fse_delay.reight_model.predict(df)[0])
    return result
