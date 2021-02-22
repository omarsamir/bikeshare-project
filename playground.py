import pandas as pd

df = pd.read_csv("chicago.csv")
#print(df.head())  # start by viewing the first few rows of the dataset!

#   What columns are in this dataset?
print('-----------')
#print(df.columns)

# value counts
#print('-----------')
#counter = df[df.columns].isnull().all(axis=1).sum()
#print(counter)

#print(df[df.columns[2]].dtype)
#print(df.dtypes)

print(df['Start Time'].dtype)
df['Start Time'] = pd.to_datetime(df['Start Time'])
#print(df['Start Time'].dtype)
#print(df['Start Time'].dt.hour)
df['hour'] = df['Start Time'].dt.hour
print(df['hour'])
print(df.mode()['hour'][0])
print(df['hour'].mode().iat[0])