# -*- coding: utf-8 -*-
"""
Created on Mon May 12 09:54:07 2025

@author: zhang
"""

# Download EU data
# Consumption 2009-01-01 to 2024-07-01
import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from ecbdata import ecbdata
"something wrong with the api download so i change save 2 files in raw data to use"
#df = ecbdata.get_series('MNA.Q.Y.I9.W0.S1M.S1.D.P31._Z._Z._T.EUR.V.N')
df = pd.read_csv("consumption.csv")
df1 = ecbdata.get_series('DWA.Q.I9.S14.A.LE.NUN._Z.EUR.S.N')
eu_finance = ecbdata.get_series('DWA.Q.I9.S14.A.LE.F51M._Z.EUR.S.N')
#eu_income = ecbdata.get_series("QSA.Q.N.I9.W0.S1M.S1._Z.B.B6G._Z._Z._Z.XDC._T.S.V.N._T")
eu_income = pd.read_excel("eu_income.xlsx")
# Save data to CSV
df.to_csv("D:/utokyo/python/graspp-25S-Wealth-Consumption/src/raw data/consumption.csv")
df1.to_csv("D:/utokyo/python/graspp-25S-Wealth-Consumption/src/raw data/housing-wealth.csv")

# Now ready to manipulate data
data = df[['TIME_PERIOD','OBS_VALUE']].dropna()
data.head(2)

#Manipulate to what we want
data = df[['TIME_PERIOD','OBS_VALUE']].dropna()
data.head(2)
data = data.rename({'TIME_PERIOD' : 'date','OBS_VALUE':'consumption'},axis=1)
data.date = pd.PeriodIndex(data.date, freq='Q').to_timestamp()
data = data[(data['date'] >= '2009-01-01') & (data['date']<= '2024-07-01')]

data1= df1[['TIME_PERIOD','OBS_VALUE']].dropna()
data1 = data1.rename({'TIME_PERIOD' : 'date','OBS_VALUE':'housing wealth'},axis=1)
data1.date = pd.PeriodIndex(data1.date, freq='Q').to_timestamp()
data1 = data1[(data1['date'] >= '2009-01-01') & (data1['date']<= '2024-07-01')]

#Consumption from 2009-01-01 to 2024-07-01
eu_consum= data
#Housing wealth from 2009-01-01 to 2024-07-01
eu_housing = data1
#financial wealth from 2009-01-01 to 2024-07-01
eu_finance = eu_finance[['TIME_PERIOD','OBS_VALUE']].dropna()
eu_finance = eu_finance.rename({'TIME_PERIOD' : 'date','OBS_VALUE':'financial wealth'},axis=1)
eu_finance.date = pd.PeriodIndex(eu_finance.date, freq='Q').to_timestamp()
eu_finance = eu_finance[(eu_finance['date'] >= '2009-01-01') & (eu_finance['date']<= '2024-07-01')]
# income 
eu_income = eu_income[['DATE','OBS.VALUE']].dropna()
eu_income = eu_income.rename({'DATE' : 'date','OBS.VALUE':'income'},axis=1)
eu_income.date = pd.PeriodIndex(eu_income.date, freq='Q').to_timestamp()
eu_income = eu_income[(eu_income['date'] >= '2009-01-01') & (eu_income['date']<= '2024-07-01')]

#merge the data 
df1 = pd.merge(eu_consum, eu_finance, how='inner', on='date')
df2 = pd.merge(eu_housing, eu_income, how='inner', on='date')
df_merge = pd.merge(df1, df2, how='inner', on='date')
df_merge.head(10)



#scatter plot
# set variables
value_columns = ['consumption', 'housing wealth', 'financial wealth', 'income']
data_for_plot = df_merge[value_columns]

# Scatter Plots
sns.pairplot(data_for_plot, kind="reg", diag_kind="kde", plot_kws={"line_kws": {"color": "red"}})
plt.suptitle("Scatter Plots with Regression Lines", y=1.02)
plt.tight_layout()
plt.show()

import numpy as np 

# Create log-transformed variables
df_merge["log_household_consumption"] = np.log(df_merge["consumption"])
df_merge["log housing wealth"] = np.log(df_merge["housing wealth"])
df_merge["log_financial_wealth"] = np.log(df_merge["financial wealth"])
df_merge["log_employment_income"] = np.log(df_merge["income"])

#OLS
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Prepare independent variables
X = df_merge[["log housing wealth", "log_financial_wealth", "log_employment_income"]]
X = sm.add_constant(X)  # constant term

# Prepare dependent variable
y = df_merge["log_household_consumption"]

# Run OLS regression
model = sm.OLS(y, X).fit()

# Show results
print(model.summary())

#Robust OLS
# Add constant term
X = sm.add_constant(X)

# Fit OLS with robust standard errors (HC3 type)
robust_ols_model = sm.OLS(y, X).fit(cov_type='HC3')

# Show summary
print(robust_ols_model.summary())

# Fit Generalized Least Squares (assumes known structure of heteroscedasticity or correlation)
gls_model = sm.GLS(y, X).fit()

# Show summary
print(gls_model.summary())

"""
#Next consider percentage change quarterly and yearly# The result is so bad and I don't think we should present it'

df_merge["consumption_change_pct_q"] = df_merge['consumption'].pct_change(1).multiply(100).dropna()
df_merge["housing wealth pct_q"] = df_merge["housing wealth"].pct_change(1).multiply(100).dropna()
df_merge["financial wealth pct_q"] = df_merge["financial wealth"].pct_change(1).multiply(100).dropna()
df_merge["income pct_q"] = df_merge["income"].pct_change(1).multiply(100).dropna()

df_merge["consumption_change_pct_y"] = df_merge['consumption'].pct_change(4).multiply(100).dropna()
df_merge["housing wealth pct_y"] = df_merge["housing wealth"].pct_change(4).multiply(100).dropna()
df_merge["financial wealth pct_y"] = df_merge["financial wealth"].pct_change(4).multiply(100).dropna()
df_merge["income pct_y"] = df_merge["income"].pct_change(4).multiply(100).dropna()

#Robust ols
y = df_merge["consumption_change_pct_q"].dropna()  # ∆log C_t
X = df_merge[["housing wealth pct_q","financial wealth pct_q","income pct_q"]].dropna()
X = sm.add_constant(X)

model = sm.OLS(y, X).fit(cov_type="HC3")  # Use robust SE due to potential non-normality
print(model.summary())
"""




