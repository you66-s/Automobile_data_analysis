# Hands-on lab: Exploratory Data Analysis - Laptops Pricing dataset
In this lab, you will explore **the effect of different features on the price of laptops**.
## Objectives
After completing this lab, i am able be able to:
- Visualize individual feature patterns
- Run descriptive statistical analysis on the dataset
- Use groups and pivot tables to find the effect of categorical variables on price
- Use Pearson Correlation to measure the interdependence between variables
## Tasks
### Task 1 - Visualize individual feature patterns
regression plots for each of the parameters "CPU_frequency", "Screen_Size_inch" and "Weight_pounds" against "Price". Also, print the value of correlation of each feature with "Price".
### Task 2 - Descriptive Statistical Analysis
statistical description of all the features being used in the data set. Include "object" data types as well.
### Task 3 - GroupBy and Pivot Tables
Group the parameters "GPU", "CPU_core" and "Price" to make a pivot table and visualize this connection using the pcolor plot.
### Task 4 - Pearson Correlation and p-values
Use the scipy.stats.pearsonr() function to evaluate the Pearson Coefficient and the p-values for each parameter tested above. This will help you determine the parameters most likely to have a strong effect on the price of the laptops