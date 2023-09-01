"""
Author: Onur Aslan
Date: 2023-08-21
Objective: main function
"""
import numpy as np
from data_fetcher import Data_fetcher
from data_visual import DataVisual

def log_dif(df):
    """
    Calculating log difference of series in pandas dataframe

    Args:
        df (pandas dataframe): _description_
    """
    for col in ['GE', 'SP500']:
        df['daily_' + col] = np.log(df[col]) - np.log(df[col].shift(1))
    
    return df

def daily_risk_free(pd_df):
    """
    Calculating daily risk-free returns

    Args:
        pd_df (pandas dataframe): _description_
    """
    # Calculating delta days in subsequent days
    pd_df['date'] = pd_df.index
    pd_df['date_delta'] = (pd_df['date'] - pd_df['date'].shift(1)).dt.days
    pd_df.loc['2000-01-03', 'date_delta'] = 0

    # Calculating daily risk-free
    pd_df['daily_risk_free'] = np.log(1 + 0.01 * pd_df['DGS3MO'] * pd_df['date_delta'] / 360)

    # Calculating daily risk-free for GE and SP500
    pd_df['daily_GE_risk_free'] = pd_df['daily_GE'] - pd_df['daily_risk_free']
    pd_df['daily_SP500_risk_free'] = pd_df['daily_SP500'] - pd_df['daily_risk_free']

    return pd_df



def main():
    """
    Main function of the code
    """
    
    # list_tickers = ['BAC', 'GE', 'JDSU', 'XOM', '^GSPC', 'DGS3MO', 'DGS1', 'DGS5', 'DGS10', 'DAAA', 'DBAA', 'DCOILWTICO']

    list_tickers = ['GE', '^GSPC'] # GE stock, SP500
    fetcher_ticker = Data_fetcher(list_tickers) # creating an object

    list_tres = ['^IRX'] # US Treasury 13-week bond rate
    fetcher_tres = Data_fetcher(list_tres) # creating an object

    visualizer = DataVisual() # creating an object
   

    # Downloading stocks data
    # fetcher1.print_ticker_info()
    data_tickers = fetcher_ticker.create_dataframe()
    data_tickers_close = data_tickers.loc[:, 'Close'].copy()
    data_tickers_close.rename(columns={'^GSPC':'SP500'}, inplace=True)
    # print(data_tickers_close.head())

    # Downloading bond rate data
    # fetcher_tres.print_ticker_info()
    data_tres = fetcher_tres.create_dataframe()
    data_tres.rename(columns={'Close':'DGS3MO'}, inplace=True)
    # print(data_tres.head())

    # Joining two dataframes above
    data_final = data_tickers_close.merge(data_tres['DGS3MO'], on='Date')

    # print(data_final.head())

    # Visualizing stocks, index and bond rate
    # visualizer.plt_time_series(data_final, y_axis_title="Price", title='GE', feature='GE')
    # visualizer.plt_time_series(data_final, y_axis_title="Value", title='S&P 500', feature='SP500')
    # visualizer.plt_time_series(data_final, y_axis_title="Rate", title='13-Week Treasury Rate (Constant Maturity)', feature='DGS3MO')

    # Calculating daily excess returns
    data_returns = log_dif(data_final)
    # print(data_returns.head())

    # Calculating daily risk-free rate
    data_risk_free = daily_risk_free(data_returns)
    # print(data_risk_free.dtypes)
    # print(data_risk_free.head(20))

    # Plotting daily_GE_risk_free vs. daily_SP500_risk_free
    visualizer.plt_scatter(data_risk_free, 'daily_GE_risk_free', 'daily_SP500_risk_free', 
                            'daily GE risk-free', 'daily SP500 risk-free', 'Daily risk-free, GE vs. SP500')
    






if __name__ == '__main__':
    main()