import pandas as pd

#define the data variable (data = ...
data=pd.read_csv("world-happiness-report-2021.csv")

#data.info() and data.describe() are examples of pre-defined functions in pandas
print(data.info())

print(data.describe())