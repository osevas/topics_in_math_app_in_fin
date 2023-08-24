"""
Author: Onur Aslan
Date: 2023-08-21
Objective: main function
"""
from data_fetcher import Data_fetcher

def main():
    """
    Main function of the code
    """
    
    # list_tickers = ['BAC', 'GE', 'JDSU', 'XOM', '^GSPC', 'DGS3MO', 'DGS1', 'DGS5', 'DGS10', 'DAAA', 'DBAA', 'DCOILWTICO']

    list_tickers = ['GE', '^GSPC'] # GE stock, SP500
    fetcher_ticker = Data_fetcher(list_tickers)

    list_tres = ['^IRX'] # US Treasury 13-week bond rate
    fetcher_tres = Data_fetcher(list_tres)
   

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

    print(data_final.head())



if __name__ == '__main__':
    main()