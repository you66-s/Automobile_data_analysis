import pandas as pd
import numpy as np
df = pd.read_csv('auto.csv')
df.columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
              "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
              "engine-type",
              "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
              "peak-rpm", "city-mpg", "highway-mpg", "price"]
df1=df.replace('?', np.nan)
print(df1.head(20))
df=df1.dropna(axis=0, how='any')
print(df.head(20))
print(df.dtypes)
df_stats = df.describe(include='all')
df.to_excel("output.xlsx", engine='xlsxwriter')
df_stats.to_excel("stats_output.xlsx", engine='xlsxwriter')
