import tensorflow as tf

# Generate dataset
X = tf.constant([1, 2, 3, 4, 5]) 
y = tf.constant([1, 2, 3, 4, 5])

# Create model
model = tf.keras.Sequential([
  tf.keras.layers.Dense(units=1) 
])

# Compile and fit
model.compile(
  optimizer='sgd',
  loss='mean_squared_error'
)

model.fit(X, y, epochs=100)

# Make predictions
print(model.predict([6]))
