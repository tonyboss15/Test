import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'RNZPXZ6Q9FEFMEHM'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval = '60min', outputsize = 'full')
print(data)
close_data = data['4. close']
percentage_change = close_data.pct_change()
print(percentage_change)
