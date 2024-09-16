import streamlit as st
import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import datetime
import numpy as np

import CAPM_functions


st.set_page_config(page_title = 'Capital Asset Pricing Model' , 
                   page_icon = "Chat_with_upward_trend" , 
                   layout = 'wide')

st.title("CAPITAL ASSET PRICING MODEL")

# get input from user

col1 , col2 = st.columns([1,1])

with col1:
    stocks_list = st.multiselect("Choose 4 stocks : ", ('TSLA' , 'AAPL', 'NFLX' , 'MSFT' , 'MGM' , 'AMZN' , 'NVDA' , 'GOOGL'),['TSLA' , 'AAPL','AMZN' , 'GOOGL'])

with col2:  
    years = st.number_input("Number of years" , 1 , 10 )


# downloading data for SP500
try:
    end = datetime.date.today()
    start = datetime.date(datetime.date.today().year-years , datetime.date.today().month , datetime.date.today().day)
    SP500 = web.DataReader('sp500' , 'fred' , start , end)

    stocks_df = pd.DataFrame()

    print(SP500.head())


    for stock in stocks_list:
        data = yf.download(stock, period = f'{years}y')
        stocks_df[f'{stock}'] = data['Close']

    stocks_df.reset_index(inplace = True)
    SP500.reset_index(inplace = True)
    SP500.columns = ['Date','sp500']

    print(stocks_df.dtypes)
    print(SP500.dtypes)

    stocks_df = pd.merge(stocks_df, SP500 , on = 'Date' , how = 'inner')

    print(stocks_df)

    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown('Dataframe Head')
        st.dataframe(stocks_df.head() , use_container_width = True)\
        
    with col2:
        st.markdown('Dataframe Tail')
        st.dataframe(stocks_df.tail() , use_container_width = True)

    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown("PRICE OF ALL THE STOCKS")
        st.plotly_chart(CAPM_functions.interactive_plot(stocks_df))

    with col2:
        print(CAPM_functions.normalize(stocks_df))
        st.markdown("PRICE OF ALL THE STOCKS AFTER NORMALIZATION")
        st.plotly_chart(CAPM_functions.interactive_plot(CAPM_functions.normalize(stocks_df)))


    stocks_daily_return = CAPM_functions.daily_return(stocks_df)
    print(stocks_daily_return.head())


    beta = {}
    alpha = {}

    for i in stocks_daily_return.columns:
        if i != 'Date' and i != 'sp500':
            b , a = CAPM_functions.calculate_beta(stocks_daily_return , i)

            beta[i] = b
            alpha[i] = a

    print(beta , alpha)

    beta_df = pd.DataFrame(columns = ['Stock' , 'Beta Value'])
    beta_df['Stock'] = beta.keys()
    beta_df['Beta Value'] = [str(round(i,2)) for i in beta.values()]

    with col1:
        st.markdown("CALCULATED BETA VALUE")
        st.dataframe(beta_df , use_container_width = True)

    rf = 0
    rm = stocks_daily_return['sp500'].mean()*252

    return_df = pd.DataFrame()
    return_value=[]
    for stock, value in beta.items():
        return_value.append(str(round(rf + (value * (rm-rf)) , 2)))
    return_df['Stock'] = stocks_list

    return_df['Return Value'] = return_value

    with col2:
        st.markdown("CALCULATED RETURN USING CAPM")
        st.dataframe(return_df , use_container_width = True )


except:
    st.write("Please Select Valid Inputs")

