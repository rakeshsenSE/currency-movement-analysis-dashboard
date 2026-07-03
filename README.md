# 💱 Currency Movement & Financial Analytics Dashboard

An interactive, real-time Financial and Forex Analytics Dashboard built using **Python, Streamlit, Pandas, and NumPy**. This application fetches live currency and financial data directly from Yahoo Finance (`yfinance`) and computes technical indicators to generate automated trading signals.

## 🚀 Live Demo
🔗 **[View Live Dashboard](https://student-performance-analytics-dashboard-app.streamlit.app/)** 

---

## ✨ Features
* **Real-Time Data Fetching:** Seamlessly pulls historical and real-time forex rates using the Yahoo Finance API (`yfinance`).
* **Dynamic Timeframes:** Users can filter currency and market data across multiple intervals: `1y`, `5y`, `10y`, `20y`, or `max` history.
* **Technical Indicators (Moving Averages):** Computes and visualizes **20-day (MA_20)** and **50-day (MA_50)** moving averages using Pandas rolling statistics.
* **AI-Powered Trading Signals:** Implements algorithmic logic using NumPy (`np.where`) to detect crossovers and generate instantaneous **BUY** or **SELL** signals based on market trends.
* **Interactive Visualizations:** High-performance, clean, and interactive time-series line charts powered by Streamlit.

---

## 🛠️ Tech Stack & Libraries
* **Frontend/Framework:** Streamlit
* **Data Manipulation:** Pandas
* **Numerical Operations:** NumPy
* **Data Source:** Yahoo Finance API (`yfinance`)

---

## 💻 How to Run Locally

Follow these simple steps to set up and run this project on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/rakeshsenSE/currency-movement-analysis-dashboard.git]
