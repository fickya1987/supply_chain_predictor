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
1. [Data Preparation](https://github.com/vishalpuri13/supply_chain_predictor/blob/main/data_preparation.ipynb) - The major challenge at the data preparation stage is filling the missing values in the data which are a plenty. They were filled as per the following considerations:\
-Shipment Mode - Drop rows\
-Dosage - Filling by mode\
-Line Item Insurance - Mean Percentage of Line Item Insurance/Line Item Value\
-PQ date - Reverse calculation by subtracting average days from Schedule Delivery to First Price Quotation\
-PO Date - Reverse calculation by subtracting average days from Schedule Delivery to Purchase Order\
-Weights - where ID is mentioned. Taken same as mentioned ID. Remaining filled with mean\
-Freight - 0 where included in Commodity Cost, where ID is mentioned. Taken same as mentioned ID. Remaining filled with mean\

2. [Pipelines & Base Model](https://github.com/vishalpuri13/supply_chain_predictor/blob/main/preprocessing%26base_model.ipynb) - The numerical and the categorical features were transformed using different pipelines and then a combined column transformer was applied. The basemodel is inspired from the model created here. It consists of an artificial neural network with 4 hidden layers. It solves a multiclass classification problem and predicts the best mode of transport for the cargo.

3. [Model Predicting Best Mode of Transporatation](https://github.com/vishalpuri13/supply_chain_predictor/blob/main/mode_model.ipynb) - The major improvement over the base model was using ADASYN or Adaptive Synthetic sampling algorithm to generate synthetic data, since the data for the means of transportation was biased towards Air shipments and it needed to be removed. It solves a multiclass classification problem and predicts the best mode of transport for the cargo.

4. [Model Predicting Freight Costs](https://github.com/vishalpuri13/supply_chain_predictor/blob/main/freight_model.ipynb) - The problem at hand was a regression problem to predict the freight cost. First a neural network with 5 hidden layers was used but the R2 score was not as per expectation. Then a hypertuned XGBRegressor model which gave much better R2 score was finalised for deployment. 

5. [Model Predicting Possible Delay](https://github.com/vishalpuri13/supply_chain_predictor/blob/main/delay_model.ipynb) - The problem at hand was a regression problem to predict the delay in number of days. Similar to the freight cost problem, first a neural network with 5 hidden layers was used but the R2 score was not as per expectation. Then a hypertuned XGBRegressor model which gave much better R2 score was finalised for deployment.

6. [Deployment](https://github.com/vishalpuri13/supply_chain_predictor/blob/main/main2.py) - Streamlit was used to deploy the three models on cloud. The apps take user data for 12 parameters and gives outputs based on the three different models developed above.

---

## Reference

The base model is inspired from [this repository](https://github.com/MSadriAghdam/Supply-Chain-Prediction_Neural-Network-ML) created by Mohsen Sadri Aghdam.
