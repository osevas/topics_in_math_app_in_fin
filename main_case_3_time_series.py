"""
Author: Onur Aslan
Date: 2023-08-21
Objective: main.py for case 3
"""
import numpy as np
from data_fetcher import Data_fetcher
from data_visual import DataVisual
from lin_regressor import Lin_reg
from data_cleaner import DataCleaner
from data_analyzer import DataAnalyzer

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
    # 1.1 Load libraries and Federal Reserve Data
    list_tres = ['^TNX'] # US Treasury 10-year yield
    fetcher_tres = Data_fetcher(list_tres) # creating an object

    visualizer = DataVisual() # creating an object

    # Downloading bond rate data
    data_tres = fetcher_tres.create_dataframe()
    data_tres.rename(columns={'Close':'DGS10'}, inplace=True)
    # print(data_tres.head())
    # print(data_tres.tail())

    # Visualizing stocks, index and bond rate
    # visualizer.plt_time_series(data_tres, y_axis_title="Close", title='10-Year Treasury Rate', feature='DGS10')

    # Data cleaning: removing na's in column DGS10
    data_cleaner1 = DataCleaner()
    data_tres_cleaned = data_cleaner1.remove_na(data_tres, 'DGS10')

    # print(data_tres_cleaned.head())
    # print(data_tres_cleaned.shape)
    # print(data_tres_cleaned.info())

    data_dgs10 = data_cleaner1.keep_cols(data_tres_cleaned, cols=['DGS10'])
    # print(data_dgs10.head(20))

    # -----------------------------------------------------------------------------------------------------------------------
    # 1.2 Create weekly and monthly time series
    # -----------------------------------------------------------------------------------------------------------------------
    data_dgs10_weekly = data_dgs10.resample('7D').last()
    data_dgs10_monthly = data_dgs10.resample('1M').last()

    # visualizer.plt_time_series(data_dgs10_weekly, y_axis_title='DGS10 Weekly', title='DGS10 Weekly', feature='DGS10')
    # visualizer.plt_time_series(data_dgs10_monthly, y_axis_title='DGS10 Monthly', title='DGS10 Monthly', feature='DGS10')

    # print(data_dgs10_weekly.shape)
    # print(data_dgs10_monthly.shape)

    # -----------------------------------------------------------------------------------------------------------------------
    # 1.3 The ACF and PACF for daily, weekly, monthly series
    # -----------------------------------------------------------------------------------------------------------------------
    analyzer1 = DataAnalyzer(data_dgs10_weekly, 'DGS10 Weekly')
    analyzer1.acf_pacf(feature='DGS10')

    analyzer2 = DataAnalyzer(data_dgs10_monthly, 'DGS10 Monthly')
    analyzer2.acf_pacf(feature='DGS10')

    # -----------------------------------------------------------------------------------------------------------------------
    # 1.4 Conduct Augmented Dickey-Fuller Test for Unit Roots
    # -----------------------------------------------------------------------------------------------------------------------




    






if __name__ == '__main__':
    main()