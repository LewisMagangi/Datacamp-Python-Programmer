"""
read_csv() function in the pandas module is used to retrieve data from csv file
"""
"""
The head() function is used to get the first n rows.
"""
import pandas as pd
df = pd.read_csv('random.csv') 
print(df.head(7))
