import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(r"chicago.csv")

# convert the Start Time column to datetime
def convert_to_date_time(str):
    return pd.to_datetime(str,format='%Y-%m-%d %H:%M:%S')

def get_hour(str):
    return pd.to_datetime(str,format='%Y-%m-%d %H:%M:%S').hour

# pd_time = convert_to_date_time('2017-06-20 11:38:18')
# print(pd_time.hour)

df['hour'] = df['Start Time'].apply(get_hour)
print(df.loc[:,['Start Time','hour']].head(5))

# df['Start Time'] = pd.to_datetime(df['Start Time'],format='%Y-%m-%d %H:%M:%S')
# print(df['Start Time'])

# extract hour from the Start Time column to create an hour column
# df['hour'] = df['Start Time'].hour
# print(df['hour'])

# find the most common hour (from 0 to 23)
# print(df['hour'].value_counts())
popular_hour = df['hour'].value_counts().keys()[0]

    
print('Most Frequent Start Hour:', popular_hour)
