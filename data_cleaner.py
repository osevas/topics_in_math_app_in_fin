"""
Objective: creating object that cleans, transforms data
Author: Onur S. Aslan
Date: 2023-03-26
"""
import pandas as pd

class DataCleaner:
    """
    Object that is tasked to clean, transform data
    """
    def change_date_format(self, df):
        """
        Changing date format from mm/dd/yyyy to yyyy-mm-dd
        """
        df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
        return df
    
    def make_date_index(self, df):
        """
        Making date column index

        Args:
            df (dataframe): _description_
        """
        df.set_index('Date', inplace=True)
        return df
    
    def week_day(self, df):
        """
        creating column that shows weekdays of date index
        Args:
            df (pandas dataframe): _description_
        """
        df['weekday'] = df.index.strftime('%A')
        return df
    
    def fiscal_week(self, df):
        """
        creating a column that shows fiscal week
        Args:
            df (pandas dataframe): _description_
        """
        df['fiscal_week'] = df.index.strftime('%U')
        return df
    
    def remove_na(self, df, col):
        """
        removing na's in pandas dataframe

        Args:
            df (pandas dataframe): _description_
        """
        df.dropna(axis=0, subset=[col], inplace=True, ignore_index=False)
        return df
    
    def keep_cols(self, df, cols=[]):
        """
        Creating a subset dataframe with columns in col

        Args:
            df (pandas dataframe): _description_
            cols (list, optional): column names to keep. Defaults to [].

        Returns:
            _type_: _description_
        """
        df = df[cols]
        return df
