import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

cars_eda_data = pd.read_csv("automobileEDA.csv")
correlation_df = cars_eda_data[["bore", "stroke", "compression-ratio", "horsepower"]].corr()

#   Positive Linear Relationship
#sns.regplot(x="engine-size", y="price", data=cars_eda_data)



#sns.regplot(x="highway-mpg", y="price", data=cars_eda_data)
print(cars_eda_data[["peak-rpm", "price"]].corr())
#sns.regplot(x="peak-rpm", y="price", data=cars_eda_data )
#plt.show()

#   Categorical Variables
#sns.boxplot(x="body-style", y="price", data=cars_eda_data)
#sns.boxplot(x="drive-wheels", y="price", data=cars_eda_data)
#plt.show()

#   Descriptive Statistical Analysis
drive_wheels_counts = cars_eda_data["drive-wheels"].value_counts().to_frame()
drive_wheels_counts.reset_index(inplace=True)
drive_wheels_counts = drive_wheels_counts.rename(columns={"drive-wheels": "value_counts"})
drive_wheels_counts.index.name = "drive-wheels"
print(drive_wheels_counts)

engine_location_counts = cars_eda_data["engine-location"].value_counts().to_frame()
engine_location_counts.reset_index(inplace=True)
engine_location_counts = engine_location_counts.rename(columns={"engine-location": "value_counts"})
engine_location_counts.index.name = "engine-location"
print(engine_location_counts)

#   Basics of Grouping
print(cars_eda_data["drive-wheels"].unique())

cars_group_one = cars_eda_data[["drive-wheels", "body-style", "price"]]
cars_grouped = cars_group_one.groupby("drive-wheels").agg({"price": ["mean", "sum"]})
print("groupBy: " , cars_grouped)

cars_gptest = cars_eda_data[['drive-wheels','body-style','price']]
grouped_1 = cars_gptest.groupby(["drive-wheels", "body-style"], as_index=False).agg({"price": "mean"})
print(grouped_1)

#pivot table        is like an Excel spreadsheet, with one variable along the column and another along the row.
grouped_pivot = grouped_1.pivot(index="drive-wheels", columns="body-style").fillna(0)
print("\n", grouped_pivot)

qst4 = cars_eda_data[["body-style", "price"]]
qst_grouped = qst4.groupby("body-style", as_index=False).agg({"price": "mean"})
print(qst_grouped)

# heatMap Visualization
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap="RdBu")
#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=0)

fig.colorbar(im)
#plt.show()

#   Correlation and Causation
pearson_coef, p_value = stats.pearsonr(cars_eda_data["wheel-base"], cars_eda_data["price"])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)  # P-value < 0.001 => the correlation between wheel-base and price is statistically significant,