import numpy as np
import pandas as pd

df = pd.read_csv("auto.csv")
df.columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
              "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
              "engine-type",
              "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
              "peak-rpm", "city-mpg", "highway-mpg", "price"]
print(df.head(10))
print("\n ---------------------- Data After Preprocessing ----------------------\n")
print("------------- Replace NaN values with Average -------------")
df1 = df.replace("?", np.nan)
print(df1.head(10))
describe = df1['normalized-losses'].describe()
print(describe)
df1['normalized-losses'] = df1['normalized-losses'].replace(np.nan, describe['freq'])
stats_described = df1.describe()
stats_described.to_excel('stats_after_pre_processing.xlsx', engine='xlsxwriter')

