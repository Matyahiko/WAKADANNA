import pandas as pd
import numpy as np
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt

#stooqでデータを取得
start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2020, 1, 1)
brand = '9984.JP'
df = web.DataReader("brand","stooq", start, end)
print(df.head())