# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 13:36:40 2023

@author: amrit
"""

import yfinance as yf
import streamlit as st
import plotly.graph_objects as go

# Title of the app
st.title('Live Stock Data with Candlestick Chart from Yahoo Finance')

# Input fields for user input
ticker = st.text_input('Enter the stock ticker symbol (e.g., IREDA.NS):')
period = st.selectbox('Select the period:', ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'))
interval = st.selectbox('Select the interval:', ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'))

# Button to fetch the data
if st.button('Fetch Data'):
    if ticker:
        with st.spinner('Fetching data...'):
            data = yf.download(tickers=ticker, period=period, interval=interval)
            st.write(f"Displaying {interval} candlestick chart for {ticker}")
            
            # Check if data is empty
            if not data.empty:
                # Candlestick chart
                fig = go.Figure(data=[go.Candlestick(
                    x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'],
                    name='Candlestick')])
                
                # Update the layout
                fig.update_layout(
                    title='Candlestick Chart',
                    yaxis_title='Stock Price',
                    xaxis_title='Date'
                )
                
                # Display the candlestick chart
                st.plotly_chart(fig, use_container_width=True)
                
                # Display the latest 50 data rows in a tabular format
                st.write("Latest 50 Data Rows:")
                st.dataframe(data.tail(50))  # Show the last 50 rows of the dataframe
            else:
                st.error('No data found for the selected ticker.')
    else:
        st.error('Please enter a stock ticker symbol.')

#
