pip install ecbdata 


import pandas as pd
from ecbdata import ecbdata
import matplotlib.pyplot as plt
#Download the data
df = ecbdata.get_series('MNA.Q.Y.I9.W0.S1M.S1.D.P31._Z._Z._T.EUR.V.N')
df1 = ecbdata.get_series('DWA.Q.I9.S14.A.LE.NUN.HST.EUR.S.N')

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