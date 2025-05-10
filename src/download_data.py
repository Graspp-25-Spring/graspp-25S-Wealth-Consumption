import pandas as pd
from ecbdata import ecbdata
import matplotlib.pyplot as plt

# Make sure to install ecbdata first
# Run this line in terminal if not installed:
# pip install ecbdata

# Download the data
df = ecbdata.get_series('MNA.Q.Y.I9.W0.S1M.S1.D.P31._Z._Z._T.EUR.V.N')
df1 = ecbdata.get_series('DWA.Q.I9.S14.A.LE.NUN.HST.EUR.S.N')

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

#Merge and present
df_merge = pd.merge(
    data, data1,
    
    how='inner', on =['date','UNIT_MEASURE']
    
)
df_merge.head(10)

plt.figure(figsize=(10, 6))
plt.plot(df_merge['date'], df_merge['consumption'], label='Consumption')
plt.plot(df_merge['date'], df_merge['housing wealth'], label='Housing wealth')
plt.xlabel('Date')
plt.ylabel('EUR')
plt.title('Consumption and housing wealth Over Time')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Descriptive statistics
plt.figure()
plt.title('Consumption')
df_merge['consumption'].describe().drop(['count'],axis=0).plot(kind ='bar')
plt.figure()
plt.title('Housing wealth')
df_merge['housing wealth'].describe().drop(['count'],axis=0).plot(kind ='bar')


#Percentage change over consumption and wealth
consumption_change_pct = data['consumption'].pct_change(1).multiply(100).dropna()
wealth_change_pct = data1['housing wealth'].pct_change(1).multiply(100).dropna()

'change it to histogram'
import seaborn as sns
sns.histplot(data= consumption_change_pct) 
plt.title('seasonal change of consumption')
sns.histplot(wealth_change_pct)
wealth_change_pct_year = data1['housing wealth'].pct_change(4).multiply(100).dropna()
sns.histplot(wealth_change_pct_year)
consumption_change_pct_year = data['consumption'].pct_change(4).multiply(100).dropna()
sns.histplot(consumption_change_pct_year)
