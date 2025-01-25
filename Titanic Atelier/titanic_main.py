import pandas as pd

titanic_data = pd.read_csv('Titanic-Dataset.csv')

def names(dataset, name, t):
    for i in range(len(dataset['Name'])):
        if name in dataset['Name'][i]:
            dataset['Name'][i] = t

names(titanic_data, name='Miss.', t="miss")
names(titanic_data, name='Mrs.', t="mrs")
names(titanic_data, name='Mr.', t="mr")
names(titanic_data, name='Dr.', t="dr")
names(titanic_data, name='Master.', t="master")


print(titanic_data["Name"].head())

