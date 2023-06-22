# Cryptocurrency Price Predictor

This project contains a cryptocurrency price predictor which uses an LSTM to predict future cryptocurrency prices using time series data. It is created using python flask and TensorFlow frameworks. It predicts the prices of different cryptocurrencies using historical data they display the output using graphs comparing the actual vs predicted graphs.

<img src="https://i.ibb.co/JtYxMwS/Screenshot-9.png" alt="Screenshot-9" border="0">

## Methodology
### 1. Dataset Selection
<img src="https://github.com/vinz3y/crypto-price-predictor/assets/68130377/4ed68d14-cbb7-423b-a685-5f8f601cc824"  border="0">

### 2. Dataset Preprocessing
<img src="https://github.com/vinz3y/crypto-price-predictor/assets/68130377/26c66345-4feb-49de-946d-d047c009bf76"  border="0">

### 3. Creating and Training the Model
* An LSTM (Long Short Term Memory) Model is created to forecast future prices.<br>
* It is a variety of recurrent neural networks (RNNs) that are capable of learning long-term dependencies, especially in sequence prediction problems.<br>
* Commonly used for making predictions based on time series data.<br>
* The LSTM Model is trained using the scaled data, and the trained model is dumped to a pickle (.pkl) file.<br>
* A Separate trained model is created for each cryptocurrency coin.<br>

### 4. Creating the Web App
* Flask was used to create this web application.<br>
* All the trained models included in the path of the web application are called when forecasting the price of the relevant coin.<br>
* Plotly which is a Python library, was used to display price prediction graphs and analyze them.<br>
* Testing data was obtained from Yahoo Finance to get the latest prices.

## Demonstration
https://youtu.be/NFi8Iwb4-fw

## Frameworks Used
* Tensorflow<br>
* Python Flask<br>
* Plotly<br>
* Bootstraps
