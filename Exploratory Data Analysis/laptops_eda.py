import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

laptops_eda = pd.read_csv("laptop_pricing_dataset_mod2.csv")

#   Task 1 - Visualize individual feature patterns
#sns.regplot(x=laptops_eda["CPU_frequency"], y=laptops_eda["Price"], data=laptops_eda)
plt.ylim(0,)
#plt.show()
#sns.regplot(x=laptops_eda["Screen_Size_inch"], y=laptops_eda["Price"], data=laptops_eda)
plt.ylim(0,)
#plt.show()
#sns.regplot(x=laptops_eda["Weight_pounds"], y=laptops_eda["Price"], data=laptops_eda)
plt.ylim(0,)
#plt.show()

#Correlation of attr with price
cpu_freq_correlation, cpu_freq_p_value = stats.pearsonr(laptops_eda["CPU_frequency"], laptops_eda["Price"])
screen_size_correlation, screen_size_p_value = stats.pearsonr(laptops_eda["Screen_Size_inch"], laptops_eda["Price"])
weight_pounds_correlation, weight_pounds_p_value = stats.pearsonr(laptops_eda["Weight_pounds"], laptops_eda["Price"])

# Categorical features
sns.boxplot(x="OS", y="Price", data=laptops_eda)
#plt.show()
sns.boxplot(x="OS", y="Price", data=laptops_eda)
#plt.show()
sns.boxplot(x="RAM_GB", y="Price", data=laptops_eda)
#plt.show()
sns.boxplot(x="Category", y="Price", data=laptops_eda)
#plt.show()
sns.boxplot(x="GPU", y="Price", data=laptops_eda)
#plt.show()
sns.boxplot(x="CPU_core", y="Price", data=laptops_eda)
#plt.show()
sns.boxplot(x="Storage_GB_SSD", y="Price", data=laptops_eda)
#plt.show()

#   Task 2 - Descriptive Statistical Analysis of all the features being used in the data set
dataset_cols_label = list(laptops_eda.columns)
dataset_cols_label.pop(0)
dataset_cols_label.pop(0)

laptops_eda_stats = laptops_eda.describe(include=["object"])

#   Task 3 - GroupBy and Pivot Tables
grouped_data = laptops_eda.groupby(["GPU", 'CPU_core'], as_index=False).agg({"Price": "mean"})
grouped_pivot2 = grouped_data.pivot(index="GPU", columns="CPU_core")

#   Task 4 - Pearson Correlation and p-values
gpu_coeff_pears, gpu_p_value = stats.pearsonr(laptops_eda["GPU"], laptops_eda["Price"])
CPU_core_coeff_pears, CPU_core_p_value = stats.pearsonr(laptops_eda["CPU_core"], laptops_eda["Price"])
