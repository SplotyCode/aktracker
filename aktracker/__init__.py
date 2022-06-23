import pymysql

#pymysql.install_as_MySQLdb()

import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info

print("AAA")
#print(msft.info)
print("BBB")
# Get the data for the stock AAPL
data = yf.download('AAPL','2016-01-01','2019-08-01')
print(data)