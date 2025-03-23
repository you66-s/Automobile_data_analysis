import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("kc_house_data_NaN.csv")

sns.boxplot(data=data, x='waterfront', y='price')
plt.xlabel('Waterfront'); plt.ylabel('Price')
plt.show(); plt.close()

sns.regplot(data=data, x='sqft_above', y='price')
plt.xlabel('sqft_above'); plt.ylabel('Price')
plt.show(); plt.close()