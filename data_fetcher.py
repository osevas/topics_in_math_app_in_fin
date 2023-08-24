"""
Author: Onur Aslan
Date: 2023-08-21
Objective: creating object data_fetcher
"""
# Libraries
import yfinance as yf
import pandas as pd


class Data_fetcher:
    """
    object that will acquire data from Yahoo Finance
    """
    def __init__(self, stock_names:list):
        """Initializing an object with stock_names

        Args:
            stock_names (list): list of names of the stocks
        """
        self.tickers = stock_names
    
    def print_ticker_info(self):
        """
        Prints summary info of one ticker

        Returns:
            _type_: _description_
        """
        ticker = yf.Ticker(self.tickers[0])
        print(ticker.info)
        return None
    
    def create_dataframe(self, start_date='2000-01-03', end_date='2013-05-31') -> pd.DataFrame:
        """
        Downloads ticker information and saves them in pandas dataframe

        Returns:
            pd.DataFrame: _description_
        """
        df = yf.download(self.tickers, start=start_date, end=end_date)
        return df
