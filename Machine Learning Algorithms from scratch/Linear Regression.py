import numpy as np

#training data
x_train = np.array([1, 2, 3, 4, 5])
y_train = np.array([1, 3, 2, 3, 5])

#model initialization
m = 0
c = 0

#learning rate
lr = 0.01

for epoch in range(4000):
    
    #calculate predictions
    y_pred = m*x_train + c
    
    #calculate error
    error = y_pred - y_train
    
    #update m and c
    m = m - lr*error.dot(x_train)
    c = c - lr*error.sum()
    
print(m, c)
