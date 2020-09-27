import numpy as np
import matplotlib.pyplot as plt # To visualize
import pandas as pd # To read data
from sklearn.linear_model import LinearRegression
data = pd.read_csv('S:\Marwadi college\sem-4\Project\s1.csv')
data['Student Marks']= pd.DatetimeIndex(data['raisedhands']).year
X = data.iloc[:, 15].values.reshape(-1, 1)
Y = data.iloc[:, 6].values.reshape(-1, 1)
lr = LinearRegression()
lr.fit(X, Y)
r_sq=lr.score(X,Y)
print('coefficient of determination:', r_sq)
print('intercept:', lr.intercept_)
print('slope:', lr.coef_)
Y_pred = lr.predict(X)
print('predicted response:', Y_pred, sep='\n')
plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.show()
