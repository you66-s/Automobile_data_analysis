# Insurance Cost Analysis
In this project, we will perform analytics operations on an insurance database that uses the below mentioned parameters.

| Parameter       | Description                         | Content type        |
|---------------|---------------------------------|--------------------|
| `age`         | Age in years                    | integer           |
| `gender`      | Male or Female                  | integer (1 or 2)  |
| `bmi`         | Body mass index                 | float             |
| `no_of_children` | Number of children          | integer           |
| `smoker`      | Whether smoker or not           | integer (0 or 1)  |
| `region`      | Which US region - NW, NE, SW, SE | integer (1,2,3 or 4 respectively) |
| `charges`     | Annual Insurance charges in USD | float             |

#   Objectives
1. **Load** the data as a **pandas**4 DataFrame.
2. **Clean** the data, handling any blank entries.
3. **Perform Exploratory Data Analysis (EDA)** to identify attributes that most affect the charges.
4. **Develop** single-variable and multi-variable **Linear Regression** models to predict the charges.
5. Use **Ridge Regression** to refine the performance of Linear Regression models.