import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Currency & Forex Analytics" , layout="wide")
st.title("Currency Movement And Financial Analytics DashBoard")

st.sidebar.header("Filter Settings")
currency_pair=st.sidebar.selectbox("Select Currency Pair:",["BDT=X","EURUSD=X","GBPUSD=X","AUDUSD=X","USDJPY=X","GBPJPY=X"])
period=st.sidebar.selectbox("Select Period:",["1y","5y","10y","15y","20y","max"])

@st.cache_data
def load_forex_data(ticker,time_period):
  data = yf.download(ticker , period=time_period)
  data.columns = data.columns.get_level_values(0)
  return data

df = load_forex_data(currency_pair,period)

df['MA_20'] = df['Close'].rolling(window=20).mean()
df['MA_50'] = df['Close'].rolling(window=50).mean()


col1,col2,col3,col4=st.columns(4)

with col1:
  st.metric(label="Current Exchange Rate" , value=f"{df['Close'].iloc[-1].round(2)}")

with col2:
  total_change=df['Close'].iloc[-1] - df['Close'].iloc[0].round(2)
  st.metric(label="Overall Price Change in period" , value=f"{total_change}")

with col3:
  max_price=df['High'].max().round(2)
  st.metric(label="Highest Price : " , value=f"{max_price}")

with col4:
  min_price=df['Low'].min().round(2)
  st.metric(label="Lowest Price : " , value=f"{min_price}")


df['Signal'] = np.where(df['MA_20'] > df['MA_50'] , "BUY","SELL")
latest_signal=df['Signal'].iloc[-1]
st.subheader("AI technical Trading Signal")

if "BUY" in latest_signal:
  st.success(f"Market Trend is Bullish! Current Signal: **{latest_signal}**")

else:
  st.error(f"Market Trend is Bearish! Current Signal: **{latest_signal}**")


st.subheader("📈 Price Movement vs Moving Averages")
st.line_chart(df[['Close','MA_20','MA_50']])

st.subheader("Raw Data Table")
st.dataframe(df.tail(150))