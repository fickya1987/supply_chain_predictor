# Supply Chain Predictor
## [Logistics Planner App](https://share.streamlit.io/vishalpuri13/supply_chain_predictor/main/main2.py)

---

## Project Description

Supply Chain is a vast domain and includes multiple stages from procurement of raw material to delivering finished goods to the customer. The one thing which is necessary at every stage is transport of finished/semi-finished/raw goods and it is especially challenging if the movement of goods has to be across borders. The project aims to augment logistics decision making and transportation planning  for international shipments. The machine learning model/neural network will learn from the past behaviours of transacting parties (fed to the model in the form of transactional data) and will predict best timelines and freight cost considerations which a supply chain manager can use for better planning and decision making.

---

## Data For Prototype

The data used to develop the protoype is USAID medical supply data taken from [here](https://data.usaid.gov/HIV-AIDS/Supply-Chain-Shipment-Pricing-Data/a3rc-nmf6). It contains 10300 shipments to 43 countries through 73 vendors supplied from 88 manufacturing sites. It contains quote-delivery timelines, product descriptions including  weights & prices and delivery costs ![image](https://user-images.githubusercontent.com/58810725/144333560-7d741885-3d03-4081-80bd-db8f4ad07c98.png)


1. Data Preparation
2. Pipelines & Base Model
3. Model Predicting Best Mode of Transporatation
4. Model Predicting Freight Costs
5. Model Predicting Posiible Delay 
6. Streamlit Deployment
