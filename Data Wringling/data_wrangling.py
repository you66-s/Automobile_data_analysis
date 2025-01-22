#  Data Wrangling is converting data from an initial format to a format that may be better for analysis.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
cars_data = pd.read_csv("auto.csv", names=headers)
cars_data.replace("?", np.nan, inplace=True)    # replace ? by NaN

missing_data = cars_data.isnull()

for instance in missing_data.columns.values.tolist():
   print(missing_data[instance].value_counts())

#Replace by mean
normalized_losses_mean = cars_data["normalized-losses"].astype("float").mean()
stroke_mean = cars_data["stroke"].astype("float").mean()
bore_mean = cars_data["bore"].astype("float").mean()
horsepower_mean = cars_data["horsepower"].astype("float").mean()
peak_rpm_mean = cars_data["peak-rpm"].astype("float").mean()

cars_data["normalized-losses"] = cars_data["normalized-losses"].replace(np.nan, normalized_losses_mean)
cars_data["stroke"] = cars_data["stroke"].replace(np.nan, stroke_mean)
cars_data["bore"] = cars_data["bore"].replace(np.nan, bore_mean)
cars_data["horsepower"] = cars_data["horsepower"].replace(np.nan, horsepower_mean)
cars_data["peak-rpm"] = cars_data["peak-rpm"].replace(np.nan, peak_rpm_mean)

#Replace by frequency
num_of_doors_freq = cars_data["num-of-doors"].value_counts().idxmax()    #idxmax() method calculate the most common type automatically
cars_data["num-of-doors"] = cars_data["num-of-doors"].replace(np.nan, num_of_doors_freq)

#Drop the whole row
cars_data = cars_data.dropna(subset=["price"])
cars_data.reset_index(drop=True, inplace=True)

# Correct data format
#print(cars_data.dtypes)
#print(cars_data.head(5))
cars_data[["bore", "stroke"]] = cars_data[["bore", "stroke"]].astype("float")
cars_data["normalized-losses"] = cars_data["normalized-losses"].astype("float")
cars_data[["price"]] = cars_data[["price"]].astype("int")
cars_data[["peak-rpm"]] = cars_data[["peak-rpm"]].astype("float")
cars_data[["horsepower"]] = cars_data[["horsepower"]].astype("int")

#   Data Standardization

cars_data["city-L/100km"] = 235/cars_data["city-mpg"]
cars_data["highway-L/100km"] = 235/cars_data["highway-mpg"]
cars_data.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)

#   Data Normalization
#Scaling values to 0-1 range
#print(cars_data["length"].head(5))
cars_data["length"] = cars_data["length"] / cars_data["length"].max()
cars_data["width"] = cars_data["width"] / cars_data["width"].max()
cars_data["height"] = cars_data["height"] / cars_data["height"].max()
#print(cars_data[["length", "height", "width"]].head(5))

#   Binning
plt.hist(cars_data["horsepower"])
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower histogramme")
bins = np.linspace(min(cars_data["horsepower"]), max(cars_data["horsepower"]), 4)
labels= ["low", "medium", "high"]
cars_data["horsepower-binned"] = pd.cut(cars_data["horsepower"], bins, labels=labels, include_lowest=True)
print(cars_data[["horsepower", "horsepower-binned"]].head(30))

plt.bar(labels, cars_data["horsepower-binned"].value_counts())
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")

plt.hist(cars_data["horsepower"], bins=3)
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
#plt.show()

#   Indicator Variable
dummy_var1 = pd.get_dummies(cars_data["fuel-type"])
cars_data = pd.concat([cars_data, dummy_var1], axis=1)
cars_data.drop(columns=["fuel-type"], inplace=True, axis=1)

dummy_aspiration = pd.get_dummies(cars_data["aspiration"])
dummy_aspiration.rename(columns={"std": "aspiration-std", 'turbo': "aspiration-turbo"}, inplace=True)
cars_data = pd.concat([cars_data, dummy_aspiration], axis=1)
cars_data.drop(columns=["aspiration"], axis=1, inplace=True)
cars_data.to_excel("clean_cars_data.xlsx", engine='xlsxwriter')