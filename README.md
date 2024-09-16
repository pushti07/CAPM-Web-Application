# Capital Asset Pricing Model (CAPM) Web Application

This repository contains a **Streamlit** web application that allows users to calculate and analyze the **Capital Asset Pricing Model (CAPM)** for selected stocks. The app provides insights into stock returns, beta values, and normalized stock prices by pulling stock data directly from Yahoo Finance.

## Project Overview

The app enables users to:
- **Select stocks**: Choose from a list of predefined stocks (e.g., TSLA, AAPL, AMZN).
- **Choose a time period**: Input the number of years for which the stock data should be analyzed.
- **View stock data**: Display the stock prices for the selected stocks and compare them against the S&P 500.
- **Calculate daily returns**: Calculate the daily percentage return for each stock.
- **Compute Beta values**: Calculate the Beta value of each stock, which measures its volatility relative to the market (S&P 500).
- **Calculate expected returns**: Use the CAPM formula to calculate the expected return for each stock based on its Beta.

## Features

### 1. Stock Data Visualization
- Interactive line charts showing stock price trends over the selected period.
- Price normalization to compare how the stocks have performed relative to each other.

### 2. Beta and Return Calculation
- Compute Beta for each stock, representing its risk in relation to the market.
- Calculate expected stock returns using the CAPM formula: 
  \[
  \text{Expected Return} = R_f + \beta (R_m - R_f)
  \]
  where \( R_f \) is the risk-free rate, and \( R_m \) is the market return.

### 3. Stock Data Analysis
- Interactive visualizations to show the stock prices before and after normalization.
- DataFrames for quick analysis of calculated Beta values and returns.

## How It Works

The web app uses the following key libraries:

- **Streamlit**: To create the interactive web application.
- **Pandas**: For data manipulation.
- **yfinance**: To fetch stock data from Yahoo Finance.
- **Pandas DataReader**: To get data for the S&P 500 from FRED (Federal Reserve Economic Data).
- **Plotly**: For creating interactive visualizations.

The project also includes a custom **CAPM_functions.py** file that contains helper functions for plotting, calculating daily returns, normalizing stock prices, and computing Beta values.

## Installation

To run the application locally, you'll need the following dependencies:

```bash
pip install streamlit pandas yfinance pandas_datareader numpy plotly
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CAPM-WebApp.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd CAPM-WebApp
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

The web app will open in your default browser.

## File Structure

- **app.py**: The main Streamlit application file.
- **CAPM_functions.py**: Contains helper functions to calculate returns, Beta values, and generate visualizations.
  
## Example Visualizations

- **Stock Price Trends**: Line plots showing the stock prices over the selected time period.
- **Normalized Stock Prices**: A comparison of stock prices, normalized to start from 1.
- **Beta Values**: A DataFrame showcasing the calculated Beta values for each stock.
- **CAPM Returns**: A DataFrame showing the expected returns based on CAPM calculations.
