import pymysql

#pymysql.install_as_MySQLdb()

import yfinance as yf

# Get the data for the stock AAPL
data = yf.download('AAPL','2016-01-01','2019-08-01')
print(data)