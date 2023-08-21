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
    fetcher1 = Data_fetcher('GE')
    fetcher1.print_info()

if __name__ == '__main__':
    main()