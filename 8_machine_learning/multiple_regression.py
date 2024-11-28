import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

# predictedC02 = regr.predict([[2300, 1300]])
predictedC02 = regr.predict([[3300, 1300]])
print(predictedC02)

# print(regr.coef_)