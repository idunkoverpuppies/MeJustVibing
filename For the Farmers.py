import pandas as pd
import numpy as np
import collections
import requests
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r'C:\Users\ayhan\Desktop\Harvest_CZ.xlsx', index_col=0)

df.index = pd.Series(df.index).fillna(method='ffill') # For some reason, the fillna method needs the dataframe to be
# called with Series. Supposedly (you're doing this because fillna is a method that belongs to pandas Series and DataFrame)
# Index objects don't have fillna() available directly.
# So you first convert df.index into a Series, which does have .fillna().


# Reset index and rename columns
df.reset_index(inplace=True)
df.columns = ['Crop', 'Metric'] + list(df.columns[2:]) # This is here to put column titles before years to be able to
# get the values from those columns. It also makes things more manageable,to know what is where
# Filter the rows where Metric is 'Harvest (t)', it can be any metric really but for the moment it is Harvest
yield_row = df[(df['Crop'] == 'Barley') & (df['Metric'] == 'Harvest (t)')]
# Filter the rows where Metric is 'Harvest (t)'
yield_data = df[df['Metric'] == 'Harvest (t)']
yield_data.set_index('Crop', inplace=True) # Set 'Crop' as the index
yield_row.set_index('Crop', inplace=True) # Dont knopw if this is necessary but still put it here
yield_data.columns = yield_data.columns.astype(str) # The excel has the numbers as int but to mention them I wanted them
# as str
yield_row.columns = yield_row.columns.astype(str)
year = '2013'
print(f"{year}")
print(yield_data[year])
print(yield_row['2023'])
# Now you have a clean dataframe where each row clearly belongs to a crop
# print(df.head())
plt.figure(figsize=(10,6))
barley_row = yield_row.squeeze()  # squeeze() turns single-row DataFrame into Series
barley_row.drop(['Metric'], errors='ignore').plot(marker='o')  # just in case 'Metric' sneaks in
# plt.xticks([2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
plt.title('Barley Harvest Over Years')
plt.xlabel('Year')
plt.ylabel('Harvest (t)')
plt.grid(True)
plt.show()