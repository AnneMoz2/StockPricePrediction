import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = yf.download('ESCORTS.NS', period = '5y', interval = '1d')
#  collected data has the following historical data - open, close, low, high, volume, adjusted close
# use adj close for pattern direction and prediction
print(data.head(3))
data_train = data.iloc[:1182, 4]
data_test = data.iloc[1132:,4]
steps = 7