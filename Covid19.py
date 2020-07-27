from pandas import ExcelWriter
import pandas as pd

df = pd.read_excel('covid19_0.xlsx')

df1 = (df.set_index(['Province/State', 'Country/Region', 'Lat', 'Long'])
       .stack()
       .reset_index(name='Value')
       .rename(columns={'level_2': 'Date'}))

writer = ExcelWriter('Covid19_Summary.xlsx')
df1.to_excel(writer, 'Sheet1', index=False)
writer.save()
