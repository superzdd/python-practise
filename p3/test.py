# 导入并加载数据
import pandas as pd
df = pd.read_csv('powerplant_data_edited.csv')
df.columns = ['Temperature','AP','RH','Exhaust Vacuum','Electrical output']
df.head()

df.plot(x='a',y='b',kind='scatter')