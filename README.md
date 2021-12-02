# Supply Chain Predictor
## [Logistics Planner App](https://share.streamlit.io/vishalpuri13/supply_chain_predictor/main/main2.py)
![Capture](https://user-images.githubusercontent.com/58810725/144333680-8bc1f0c3-db01-4288-99c6-07dd24f0cf55.JPG)

---

## Project Description

Supply Chain is a vast domain and includes multiple stages from procurement of raw material to delivering finished goods to the customer. The one thing which is necessary at every stage is transport of finished/semi-finished/raw goods and it is especially challenging if the movement of goods has to be across borders. The project aims to augment logistics decision making and transportation planning  for international shipments. The machine learning model/neural network will learn from the past behaviours of transacting parties (fed to the model in the form of transactional data) and will predict best timelines and freight cost considerations which a supply chain manager can use for better planning and decision making.

---

## Data For Prototype

The data used to develop the protoype is USAID medical supply data taken from [here](https://data.usaid.gov/HIV-AIDS/Supply-Chain-Shipment-Pricing-Data/a3rc-nmf6). It contains 10300 shipments to 43 countries through 73 vendors supplied from 88 manufacturing sites. It contains timelines for stages from quotation to delivery, product descriptions including  weights & prices and delivery costs.

---

## Flowchart
![Flow2](https://user-images.githubusercontent.com/58810725/144334324-3c4f4b1e-1f29-42a2-ada3-5f159162d955.jpeg)

---

## Process
The app development process consists of the following 6 stages:
1. [Data Preparation](https://github.com/vishalpuri13/supply_chain_predictor/blob/main/data_preparation.ipynb) - The major challenge at the data preparation stage is filling the missing values in the data which are a plenty. Some highlights of the data are:\
2 types Fulfill Via - From RDC(52%) and Direct Drop(48%)\
INCO Terms - N/A for RDC, 7 Inco Terms used- mostly EXW(56%),DDP(29%),FCA(8%),CIP(5.5%)\
4 Shipment modes - Air (59%), Truck (27%), Air Charter (6%), Ocean (3%), Nan (3%)\
PQ First Sent Date - NA (24%)\
PO Sent to Vendor Date - NA for RDC + Not captured (55%)\
5 Product Group - ARV (83%), HRDT(17%), 3 negligible\
6 Sub Class - Adult (64%), Pediatric (19%), HIV test(15%), HIV-Ancillary (2%), Malaria and ACT negligible\
72 Non-RDC Vendors\
48 Brands\
17 Dosage Form\
First Line Designation - Yes (68%), No(32%)\
Weight - Not defined for 40% data\
Freight Cost - Not clear for 41% data\
Insurance NAN for 3%\ They were filled as per the following considerations: 
2. [Pipelines & Base Model](https://github.com/vishalpuri13/supply_chain_predictor/blob/main/preprocessing%26base_model.ipynb)
3. [Model Predicting Best Mode of Transporatation](https://github.com/vishalpuri13/supply_chain_predictor/blob/main/mode_model.ipynb)
4. [Model Predicting Freight Costs](https://github.com/vishalpuri13/supply_chain_predictor/blob/main/freight_model.ipynb)
5. [Model Predicting Possible Delay](https://github.com/vishalpuri13/supply_chain_predictor/blob/main/delay_model.ipynb)
6. [Streamlit Deployment](https://github.com/vishalpuri13/supply_chain_predictor/blob/main/main2.py)
