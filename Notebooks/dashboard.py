# imports
import panel as pn
pn.extension('plotly')
import plotly.express as px
import pandas as pd
import hvplot
import hvplot.pandas
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from dotenv import load_dotenv
import plotly.graph_objects as go
import alpaca_trade_api as tradeapi

import warnings
warnings.filterwarnings('ignore')

df1 = pd.read_csv('../Data/AAPL - Sheet1.csv', infer_datetime_format=True, parse_dates=True, index_col='Date')

cs = go.Figure(data=[go.Candlestick(
    open = df1['Open'],
    high = df1['High'],
    low = df1['Low'],
    close = df1['Close']
)])

dashboard = pn.Tabs(
    pn.Row(cs.show())
)
df1.head()
dashboard.servable()