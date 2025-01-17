import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


try:
    laptops_data = pd.read_csv('laptop_pricing_dataset_mod1.csv')
    #laptops_data.info()
    #print(laptops_data.head(5))
except:
    print("There's an error while reading the file")

laptops_data[['Screen_Size_cm']] = np.round(laptops_data[['Screen_Size_cm']], 2)

# Missing Values Handling
laptops_data_weight_mean = np.round(laptops_data["Weight_kg"].astype("float").mean(), 2)
laptops_data["Weight_kg"] = laptops_data["Weight_kg"].replace(np.nan, laptops_data_weight_mean)

laptops_data_Screen_Size_freq = laptops_data["Screen_Size_cm"].value_counts().idxmax()
laptops_data["Screen_Size_cm"] = laptops_data["Screen_Size_cm"].replace(np.nan, laptops_data_Screen_Size_freq)

#   Fixing the data types
laptops_data[["Weight_kg", "Screen_Size_cm"]] = laptops_data[["Weight_kg", "Screen_Size_cm"]].astype("float")

#   Data Standardization
laptops_data["Weight_kg"] =np.round( 2.20462 * laptops_data["Weight_kg"], 2)
laptops_data.rename(columns={"Weight_kg": "Weight_pounds"}, inplace=True)

laptops_data["Screen_Size_cm"] = np.round(laptops_data["Screen_Size_cm"] / 2.54, 2)
laptops_data.rename(columns={"Screen_Size_cm": "Screen_Size_in"}, inplace=True)

#   Data Normalization
cpu_stats = laptops_data["CPU_frequency"].describe()
laptops_data["CPU_frequency"] = laptops_data["CPU_frequency"] / laptops_data["CPU_frequency"].max()

#   Binning
bins = np.linspace(min(laptops_data["Price"]), max(laptops_data["Price"]), 4)
group_names = ['Low', 'Medium', 'High']
laptops_data["Price-binned"] = pd.cut(laptops_data["Price"], bins, labels=group_names, include_lowest=True)
plt.bar(group_names, laptops_data["Price-binned"].value_counts())
plt.xlabel("price")
plt.ylabel("count")
plt.title("Price bins")
#plt.show()

#   Indicator variables

dummy_screens = pd.get_dummies(laptops_data["Screen"])
dummy_screens.rename(columns={"IPS Panel":'Screen-IPS_panel', 'Full HD':'Screen-Full_HD'},inplace=True)
laptops_data = pd.concat([laptops_data, dummy_screens], axis=1)
laptops_data.drop("Screen", axis=1, inplace=True)
laptops_data.to_excel("clean_laptops_data.xlsx", engine="xlsxwriter")
print(laptops_data.head(5))