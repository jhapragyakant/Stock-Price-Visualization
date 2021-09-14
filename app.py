# Importing the required libraries
import yfinance as yf
import streamlit as st
import pandas as pd
import datetime

# Title and the welcome text
st.title("Stock Price Visualization")
st.write("""
### Choose the ***company*** you want to view the **stock price** of:
""")

# Dropdown for selection of top companies
company_name = st.selectbox("Company Name", ("Apple", "Google", "Microsoft", "Adobe", "Netflix", "Facebook","Twitter"))

# Function to get the ticker Symbol
def get_tickerSymbol(company_name):
    if company_name == "Apple":
        tickerSymbol = 'AAPL'
    elif company_name == "Google":
        tickerSymbol = 'GOOGL'
    elif company_name == "Microsoft":
        tickerSymbol = 'MSFT'
    elif company_name == "Adobe":
        tickerSymbol = 'ADBE'
    elif company_name == "Netflix":
        tickerSymbol = 'NFLX'
    elif company_name == "Facebook":
        tickerSymbol = 'FB'
    elif company_name == "Twitter":
        tickerSymbol = 'TWTR'
    return tickerSymbol

# Getting company name from user and assigning ticker symbol
tickerSymbol = get_tickerSymbol(company_name)

# Getting data from this Ticker
tickerData = yf.Ticker(tickerSymbol)

# Taking input of start date and end date to show the stock price from the user
start_date = st.date_input('Start Date')
end_date = st.date_input('End Date')

## These are just the random stuff we can do with tickerData
# st.write(tickerData.info)
# st.write(tickerData.calendar)
# st.write(tickerData.recommendations)

# Getting historical prices for this Ticker
ticker_historial_data = tickerData.history(period = '1d', start = start_date, end = end_date)
# Open   High   Low    Close    Volume     Stock Splits
# This is the format of the ticker_historical_data


# Plotting the graphs
st.write("""
### Closing prices
""")
st.line_chart(ticker_historial_data.Close)

st.write("""
### Volume of shares
""")
st.line_chart(ticker_historial_data.Volume)