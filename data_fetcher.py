"""
Author: Onur Aslan
Date: 2023-08-21
Objective: creating object data_fetcher
"""
# Libraries
import yfinance as yf


class Data_fetcher:
    """
    object that will acquire data from Yahoo Finance
    """
    def __init__(self, stock_names:str):
        """Initializing an object with stock_names

        Args:
            stock_names (string): names of the stocks
        """
        self.tickers = stock_names
    
    def print_info(self):
        ge = yf.Ticker(self.tickers)
        print(ge.info)
        return None
