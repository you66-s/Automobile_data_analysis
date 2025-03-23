import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score

#Data Reading
cars_eda_df = pd.read_csv("automobileEDA.csv")

lm = LinearRegression()     # Linear Regression object creation

X = cars_eda_df[["highway-mpg"]]
Y = cars_eda_df["price"]
fit = lm.fit(X, Y)        # Cette fonction permet de entrainer le modele
Yhat = lm.predict(X)      # utilisée pour faire des prédictions avec un modèle de régression linéaire déjà entraîné
a_intercept = np.round(lm.intercept_, 2)
b_coef = np.round(lm.coef_,2)
print("intercept: ", a_intercept)
print("slope: ", b_coef)
print(f"Estimated linear model: Price = {a_intercept}{b_coef[0]}*highway-mpg")

lm1 = LinearRegression()
X1 = cars_eda_df[["engine-size"]]
lm1.fit(X1, Y)
Yhat1 = lm1.predict(X1)
a1_intercept = np.round(lm1.intercept_, 2)
b1_coef = np.round(lm1.coef_,2)
print("intercept: ", a1_intercept)
print("slope: ", b1_coef)
print(f"Estimated linear model: Price = {a1_intercept}+{b1_coef[0]}*engine-size")

# Multiple linear variable model
lm3 = LinearRegression()
Z = cars_eda_df[["horsepower", "curb-weight", 'engine-size', 'highway-mpg']]

lm3.fit(Z, Y)
pred_multi = lm3.predict(Z)
a3_intercept = np.round(lm3.intercept_, 2)
b3_coef = np.round(lm3.coef_,2)
print("intercept: ", a3_intercept)
print("slope: ", b3_coef)

lm4 = LinearRegression()
W = cars_eda_df[["normalized-losses", "highway-mpg"]]
lm4.fit(W, Y)
pred_normalized = lm4.predict(W)
a4_intercept = np.round(lm4.intercept_, 2)
b4_coef = np.round(lm4.coef_,2)
print("intercept: ", a4_intercept)
print("slope: ", b4_coef)

# Model Evaluation
plt.figure()    # ectte fonction va creer un conteneur qui va contient nos plots
sns.regplot(x=cars_eda_df["highway-mpg"], y=cars_eda_df["price"], data=cars_eda_df)
plt.ylim(0,)
plt.xlabel("Highway MPG")
plt.ylabel("Price")
#plt.show()
plt.close()

plt.figure()
sns.regplot(x=cars_eda_df["peak-rpm"], y=cars_eda_df["price"], data=cars_eda_df)
plt.title("")
plt.xlabel("peak-rpm")
plt.ylabel("Price")
plt.ylim(0,)
#plt.show()
plt.close()

#   residual plot
plt.figure()
sns.residplot(x=cars_eda_df["highway-mpg"], y=cars_eda_df["price"])
plt.title("residual plot")
#plt.show()
plt.close()

#    Polynomial Regression and Pipelines
def PlotPolly(model, indep_var, dep_var, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)
    plt.plot(indep_var, dep_var, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')
    plt.show()
    plt.close()

f = np.polyfit(cars_eda_df["highway-mpg"], cars_eda_df["price"], 3)
p = np.poly1d(f)
#PlotPolly(p, cars_eda_df["highway-mpg"], cars_eda_df["price"], "")

f11 = np.polyfit(cars_eda_df["highway-mpg"], cars_eda_df["price"], 11)
p11 = np.poly1d(f11)
#PlotPolly(p11, cars_eda_df["highway-mpg"], cars_eda_df["price"], "Order 11")

pr = PolynomialFeatures(degree=2)   #PolynomialFeatures object of degree 2
Z_pr = pr.fit_transform(Z)
z_shape = Z.shape
Z_pr_shape = Z_pr.shape

# PipeLines
input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model', LinearRegression())]
pipeline = Pipeline(input)
pipeline.fit(Z, Y)
y_pipe = pipeline.predict(Z)

# Evaluation du modele
print("\nModel 1: Simple Linear Regression: ")
print("The R-square is: ", lm.score(X, Y))     # We can say that ~49.659% of the variation of the price is explained by this simple linear model "horsepower_fit".
mse = mean_squared_error(cars_eda_df["price"], Yhat)
print('The mean square error of price and predicted value is: ', mse)

print("\nModel 2: Model 3: Polynomial Fit: ")
r_squared = r2_score()