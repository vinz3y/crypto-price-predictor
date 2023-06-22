from flask import Blueprint, render_template, url_for, request, flash
import pandas as pd 
import json
import plotly
import plotly.express as px
import numpy as np
import plotly.graph_objs as go


from sklearn.preprocessing import MinMaxScaler
import joblib


#defien that this file is a blueprint of the application
#set name of blueprint as views
views = Blueprint('views',__name__)

def getpredictions(dataset_train, filename,dataset_test ):
    training_set = dataset_train.iloc[:, 7:8].values
    
    #Load Model
    loaded_model = joblib.load(filename)

    #Getting Test Prices
    real_stock_price = dataset_test.iloc[:, 4:5].values

    #Getting the predicting prices
    dataset_total = pd.concat((dataset_train['Close'], dataset_test['Close']), axis = 0)
    inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
    sc = MinMaxScaler(feature_range = (0, 1))
    training_set_scaled = sc.fit_transform(training_set)

    inputs = inputs.reshape(-1,1)
    inputs = sc.transform(inputs)


    #Creating Test Set
    x_test = []
    for i in range(60, len(inputs)):
        x_test.append(inputs[i-60:i, 0])
        #20 days in a month

    x_test = np.array(x_test)

    x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))

    #Predicting the price and inverse transforming it
    predicted_stock_price = loaded_model.predict(x_test)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)

    #print("Predicted Stock Price" ,predicted_stock_price)
    #print("Real_stock_price" , real_stock_price)

    prediction_dates = dataset_test.iloc[:, [0]].values

    #print(prediction_dates)

    combined= np.concatenate((prediction_dates,real_stock_price, predicted_stock_price), axis=1)

    column_names = ['Date','Actual Price','Predicted Price']
    structured_data = np.core.records.fromarrays(combined.transpose(), names=','.join(column_names))

    return structured_data



@views.route('/')
def home():
    return render_template("home.html")

@views.route('/prices/btc')
def btc():
    
#Below values changes with the currency
    dataset_train = pd.read_csv('prices/coin_Bitcoin.csv')
    filename = 'model/BTC_model.pkl'
    dataset_test = pd.read_csv('test-prices/BTC-USD.csv')


    structured_data = getpredictions(dataset_train, filename,dataset_test )
    fig1 = px.line(structured_data,x= "Date", y= [ 'Date','Actual Price','Predicted Price'], title="Bitcoin  Actual Price vs Predicted Price",width=1500, height=700)
    graphJSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    data_length = len(structured_data)
    end_date = structured_data[data_length-1][0]
    end_actual_price = structured_data[data_length-1][1]
    end_actual_price = round(end_actual_price, 2)
    end_predicted_price = structured_data[data_length-1][2]
    end_predicted_price = round(end_predicted_price, 2)
    #print(end_predicted_price)

    return render_template("currencies/btc.html" , title="BTC Price", graphJSON=graphJSON , end_date=end_date, end_actual_price= end_actual_price, end_predicted_price = end_predicted_price )


@views.route('/prices/eth')
def eth():
    #Below values changes with the currency
    dataset_train = pd.read_csv('prices/coin_Ethereum.csv')
    filename = 'model/ETH_model.pkl'
    dataset_test = pd.read_csv('test-prices/ETH-USD.csv')


    structured_data = getpredictions(dataset_train, filename,dataset_test )
    fig1 = px.line(structured_data,x= "Date", y= [ 'Date','Actual Price','Predicted Price'], title="Ethereum  Actual Price vs Predicted Price",width=1500, height=700)
    graphJSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    data_length = len(structured_data)
    end_date = structured_data[data_length-1][0]
    end_actual_price = structured_data[data_length-1][1]
    end_actual_price = round(end_actual_price, 2)
    end_predicted_price = structured_data[data_length-1][2]
    end_predicted_price = round(end_predicted_price, 2)
    #print(end_predicted_price)


    return render_template("currencies/eth.html" , title="ETH Price", graphJSON=graphJSON , end_date=end_date, end_actual_price= end_actual_price, end_predicted_price = end_predicted_price )


@views.route('/prices/sol')
def sol():
    #Below values changes with the currency
    dataset_train = pd.read_csv('prices/coin_Solana.csv')
    filename = 'model/SOL_model.pkl'
    dataset_test = pd.read_csv('test-prices/SOL-USD.csv')


    structured_data = getpredictions(dataset_train, filename,dataset_test )
    fig1 = px.line(structured_data,x= "Date", y= [ 'Date','Actual Price','Predicted Price'], title="Solana  Actual Price vs Predicted Price",width=1500, height=700)
    graphJSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    data_length = len(structured_data)
    end_date = structured_data[data_length-1][0]
    end_actual_price = structured_data[data_length-1][1]
    end_actual_price = round(end_actual_price, 2)
    end_predicted_price = structured_data[data_length-1][2]
    end_predicted_price = round(end_predicted_price, 2)
    #print(end_predicted_price)

    return render_template("currencies/sol.html" , title="SOL Price", graphJSON=graphJSON , end_date=end_date, end_actual_price= end_actual_price, end_predicted_price = end_predicted_price)

@views.route('/prices/xpr')
def xrp():
    #Below values changes with the currency
    dataset_train = pd.read_csv('prices/coin_XRP.csv')
    filename = 'model/XPR_model.pkl'
    dataset_test = pd.read_csv('test-prices/XPR-USD.csv')


    structured_data = getpredictions(dataset_train, filename,dataset_test )
    fig1 = px.line(structured_data,x= "Date", y= [ 'Date','Actual Price','Predicted Price'], title="Ripple Actual Price vs Predicted Price",width=1500, height=700)
    graphJSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    data_length = len(structured_data)
    end_date = structured_data[data_length-1][0]
    end_actual_price = structured_data[data_length-1][1]
    end_actual_price = round(end_actual_price, 2)
    end_predicted_price = structured_data[data_length-1][2]
    end_predicted_price = round(end_predicted_price, 2)
    #print(end_predicted_price)

    return render_template("currencies/xrp.html" , title="Ripple Price", graphJSON=graphJSON , end_date=end_date, end_actual_price= end_actual_price, end_predicted_price = end_predicted_price )

@views.route('/prices/dot')
def dot():
    #Below values changes with the currency
    dataset_train = pd.read_csv('prices/coin_Polkadot.csv')
    filename = 'model/DOT_model.pkl'
    dataset_test = pd.read_csv('test-prices/DOT-USD.csv')


    structured_data = getpredictions(dataset_train, filename,dataset_test )
    fig1 = px.line(structured_data,x= "Date", y= [ 'Date','Actual Price','Predicted Price'], title="Polkadot Actual Predicted vs Predicted Price",width=1500, height=700)
    graphJSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    data_length = len(structured_data)
    end_date = structured_data[data_length-1][0]
    end_actual_price = structured_data[data_length-1][1]
    end_actual_price = round(end_actual_price, 2)
    end_predicted_price = structured_data[data_length-1][2]
    end_predicted_price = round(end_predicted_price, 2)
    #print(end_predicted_price)

    return render_template("currencies/dot.html" , title="Polkadot Price", graphJSON=graphJSON , end_date=end_date, end_actual_price= end_actual_price, end_predicted_price = end_predicted_price)

@views.route('/prices/ada')
def ada():

    #Below values changes with the currency
    dataset_train = pd.read_csv('prices/coin_Cardano.csv')
    filename = 'model/ADA_model.pkl'
    dataset_test = pd.read_csv('test-prices/ADA-USD.csv')


    structured_data = getpredictions(dataset_train, filename,dataset_test )
    fig1 = px.line(structured_data,x= "Date", y= [ 'Date','Actual Price','Predicted Price'], title="Cardano Coin  Actual Price vs Predicted Price",width=1500, height=700)
    graphJSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    data_length = len(structured_data)
    end_date = structured_data[data_length-1][0]
    end_actual_price = structured_data[data_length-1][1]
    end_actual_price = round(end_actual_price, 2)
    end_predicted_price = structured_data[data_length-1][2]
    end_predicted_price = round(end_predicted_price, 2)
    #print(end_predicted_price)

    return render_template("currencies/bnb.html" , title="ADA Price", graphJSON=graphJSON , end_date=end_date, end_actual_price= end_actual_price, end_predicted_price = end_predicted_price)

@views.route('/prices/bnb')
def bnb():
    #Below values changes with the currency
    dataset_train = pd.read_csv('prices/coin_BinanceCoin.csv')
    filename = 'model/BNB_model.pkl'
    dataset_test = pd.read_csv('test-prices/BNB-USD.csv')


    structured_data = getpredictions(dataset_train, filename,dataset_test )
    fig1 = px.line(structured_data,x= "Date", y= [ 'Date','Actual Price','Predicted Price'], title="Binance Coin  Actual Price vs Predicted Price",width=1500, height=700)
    graphJSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    data_length = len(structured_data)
    end_date = structured_data[data_length-1][0]
    end_actual_price = structured_data[data_length-1][1]
    end_actual_price = round(end_actual_price, 2)
    end_predicted_price = structured_data[data_length-1][2]
    end_predicted_price = round(end_predicted_price, 2)
    #print(end_predicted_price)

    return render_template("currencies/bnb.html" , title="BNB Price", graphJSON=graphJSON , end_date=end_date, end_actual_price= end_actual_price, end_predicted_price = end_predicted_price)

@views.route('/prices/doge')
def doge():
    #Below values changes with the currency
    dataset_train = pd.read_csv('prices/coin_Dogecoin.csv')
    filename = 'model/DOGE_model.pkl'
    dataset_test = pd.read_csv('test-prices/DOGE-USD.csv')


    structured_data = getpredictions(dataset_train, filename,dataset_test )
    fig1 = px.line(structured_data,x= "Date", y= [ 'Date','Actual Price','Predicted Price'], title="Dogecoin Coin  Actual Price vs Predicted Price",width=1500, height=700)
    graphJSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    data_length = len(structured_data)
    end_date = structured_data[data_length-1][0]
    end_actual_price = structured_data[data_length-1][1]
    end_actual_price = round(end_actual_price, 2)
    end_predicted_price = structured_data[data_length-1][2]
    end_predicted_price = round(end_predicted_price, 2)
    #print(end_predicted_price)

    return render_template("currencies/doge.html" , title="DOGE Price", graphJSON=graphJSON , end_date=end_date, end_actual_price= end_actual_price, end_predicted_price = end_predicted_price)