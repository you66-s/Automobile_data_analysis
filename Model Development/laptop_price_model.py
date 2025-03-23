from tkinter import Scale

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score

laptop_df = pd.read_csv("laptop_pricing_dataset_mod2.csv")

X_cpu = laptop_df[['CPU_frequency']]
Y_price = laptop_df['Price']
lm = LinearRegression()
lm.fit(X_cpu, Y_price)
pred_cpu_freq = lm.predict(X_cpu)
r_squared = lm.score(X_cpu, Y_price)
mse = mean_squared_error(Y_price, pred_cpu_freq)

# Task 2

Z = laptop_df[['CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core', 'OS', 'GPU']]
lm_multiple = LinearRegression()
lm_multiple.fit(Z, Y_price)
lm_multiple_pred = lm_multiple.predict(Z)
r_squared_multiple = lm_multiple.score(Z, Y_price)
mse_multiple = mean_squared_error(Y_price, lm_multiple_pred)

# Task 3: Polynomial Regression
def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(independent_variable.min(),independent_variable.max(),100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title(f'Polynomial Fit for Price ~ {Name}')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of laptops')
    plt.show()
    plt.close()

f_poly_3 = np.polyfit(laptop_df['CPU_frequency'], Y_price, 1)
f_poly_6 = np.polyfit(laptop_df['CPU_frequency'], Y_price, 3)
f_poly_9 = np.polyfit(laptop_df['CPU_frequency'], Y_price, 5)
p_poly_3 = np.poly1d(f_poly_3)
p_poly_6 = np.poly1d(f_poly_6)
p_poly_9 = np.poly1d(f_poly_9)

PlotPolly(p_poly_3, laptop_df['CPU_frequency'], Y_price, 'Polynomial 1 Fit for Price')
PlotPolly(p_poly_6, laptop_df['CPU_frequency'], Y_price, 'Polynomial 3 Fit for Price')
PlotPolly(p_poly_9, laptop_df['CPU_frequency'], Y_price, 'Polynomial 5 Fit for Price')

# PipeLine
steps = [('scale', StandardScaler()), ('model', LinearRegression())]
pipe = Pipeline(steps)
pipe.fit(X_cpu, Y_price)
pipe_pred = pipe.predict(X_cpu)
r2_score_pipe = pipe.score(X_cpu, Y_price)
mse_pipe = mean_squared_error(Y_price, pipe_pred)
