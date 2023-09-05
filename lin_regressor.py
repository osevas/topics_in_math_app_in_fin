"""
Objective: to create a class for linear regression
Author: https://github.com/osevas
Date: 2023-09-04
"""

# Libraries
import statsmodels.api as sm

class Lin_reg:
    """
    Class for linear regression
    """
    def fit_ols(self, y, x, missing='drop'):
        """
        Fitting ordinary-least-squares

        Args:
            y (_type_): _description_
            x (_type_): _description_

        Returns:
            _type_: _description_
        """
        x = sm.add_constant(x)
        model = sm.OLS(y, x, missing=missing)
        results = model.fit()
        # print('\nResult parameters')
        # print(results.params)
        
        # print('\nResult t-values:')
        # print(results.tvalues)
        
        print('\nModel summary:')
        print(results.summary())
        
        print('\nResiduals:')
        print('Min: {}'.format(results.resid.min()))
        print('1Q: {}'.format(results.resid.quantile(q=0.25)))
        print('Median: {}'.format(results.resid.median()))
        print('3Q: {}'.format(results.resid.quantile(q=0.75)))
        print('Max: {}'.format(results.resid.max()))
        return None
