# -*- coding: utf-8 -*-
"""
Created on Mon May 12 09:54:07 2025

@author: zhang
"""

# Download EU data
# Consumption 2009-01-01 to 2024-07-01
import pandas as pd
from ecbdata import ecbdata
df = ecbdata.get_series('MNA.Q.Y.I9.W0.S1M.S1.D.P31._Z._Z._T.EUR.V.N')
df1 = ecbdata.get_series('DWA.Q.I9.S14.A.LE.NUN._Z.EUR.S.N')
eu_finance = ecbdata.get_series('DWA.Q.I9.S14.A.LE.F51M._Z.EUR.S.N')
eu_income = ecbdata.get_series("QSA.Q.N.I9.W0.S1M.S1._Z.B.B6G._Z._Z._Z.XDC._T.S.V.N._T")
# Save data to CSV
df.to_csv("D:/utokyo/python/graspp-25S-Wealth-Consumption/src/raw data/consumption.csv")
df1.to_csv("D:/utokyo/python/graspp-25S-Wealth-Consumption/src/raw data/housing-wealth.csv")

# Now ready to manipulate data
data = df[['TIME_PERIOD','OBS_VALUE','UNIT_MEASURE']].dropna()
data.head(2)

#Manipulate to what we want
data = df[['TIME_PERIOD','OBS_VALUE','UNIT_MEASURE']].dropna()
data.head(2)
data = data.rename({'TIME_PERIOD' : 'date','OBS_VALUE':'consumption'},axis=1)
data.date = pd.PeriodIndex(data.date, freq='Q').to_timestamp()
data = data[(data['date'] >= '2009-01-01') & (data['date']<= '2024-07-01')]

data1= df1[['TIME_PERIOD','OBS_VALUE','UNIT_MEASURE']].dropna()
data1 = data1.rename({'TIME_PERIOD' : 'date','OBS_VALUE':'housing wealth'},axis=1)
data1.date = pd.PeriodIndex(data1.date, freq='Q').to_timestamp()
data1 = data1[(data1['date'] >= '2009-01-01') & (data1['date']<= '2024-07-01')]

#Consumption from 2009-01-01 to 2024-07-01
eu_consum= data
#Housing wealth from 2009-01-01 to 2024-07-01
eu_housing = data1
#financial wealth from 2009-01-01 to 2024-07-01
eu_finance = eu_finance[['TIME_PERIOD','OBS_VALUE','UNIT_MEASURE']].dropna()
eu_finance = eu_finance.rename({'TIME_PERIOD' : 'date','OBS_VALUE':'financial wealth'},axis=1)
eu_finance.date = pd.PeriodIndex(eu_finance.date, freq='Q').to_timestamp()
eu_finance = eu_finance[(eu_finance['date'] >= '2009-01-01') & (eu_finance['date']<= '2024-07-01')]
# income 
eu_income = eu_income[['TIME_PERIOD','OBS_VALUE']].dropna()
eu_income = eu_income.rename({'TIME_PERIOD' : 'date','OBS_VALUE':'income'},axis=1)
eu_income.date = pd.PeriodIndex(eu_income.date, freq='Q').to_timestamp()
eu_income = eu_income[(eu_income['date'] >= '2009-01-01') & (eu_income['date']<= '2024-07-01')]
