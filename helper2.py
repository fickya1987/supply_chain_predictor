import pandas as pd
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model

# Helper function to handle data loading and manipulation
def load_and_process_data(filepath):
    data = pd.read_csv(filepath)
    categorical_vars = ['proj_code', 'country', 'vendor', 'manu_site', 'via', 'inco']
    return {var: list(set(data[var])) for var in categorical_vars}

categorical_data = load_and_process_data('pre_encoding_data.csv')
inverse_label = {0: 'Air', 1: 'Air Charter', 2: 'Ocean', 3: 'Truck'}

# Load saved assets
preprocessor = pickle.load(open('preprocess2.pkl', 'rb'))
transport_mode_model = load_model('best_transport_mode2')
delay_model = pickle.load(open('best_delay_model.pkl', 'rb'))
freajght_model = pickle.load(open('best_freight_model.pkl', 'rb'))

def mode_prediction(df):
    p = transport_mode_model.predict(df)
    pred = pd.DataFrame(data=p)
    best_route = pred.idxmax(axis=1)[0]
    result = inverse_label.get(best_element, "Unknown Route")
    return result

def delay_prediction(df):
    result = round(delay_model.predict(df)[0])
    return result

def freight_prediction(df):
    result = round(freight_model.predict(df)[0])
    return result
