from sklearn.linear_model import LinearRegression
import numpy as np

#training data
x_train = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y_train = np.array([1, 3, 2, 3, 5])

#create linear regression object
reg = LinearRegression()

#train the model
reg.fit(x_train, y_train)

#Predict on new data
x_new = np.array([6]).reshape(-1, 1)
y_pred = reg.predict(x_new)

print(reg.coef_, reg.intercept_)
print(y_pred)
