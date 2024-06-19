import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from data_fetch import download_historical_data 
from performance import plot_closing_prices

def main():
    # Download historical price data
    symbol = 'RELIANCE.NS'
    start_date = '2024-06-01'
    end_date = datetime.today().strftime('%Y-%m-%d')
    data = download_historical_data(symbol, start_date, end_date)
    
    data = pd.DataFrame(data)
    df=data.head(10)
    print(df.to_string())
    # Plot closing prices
    plot_closing_prices(data, symbol)

if __name__ == '__main__':
    main()