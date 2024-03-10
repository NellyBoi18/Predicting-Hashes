import hashlib
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import custom_object_scope

# Encode hash strings into numerical features using hash functions
def hash_to_numeric(hash_string):
    hash_numeric = int(hashlib.sha256(hash_string.encode()).hexdigest(), 16)
    return hash_numeric

# Read historical data from CSV file
historical_data = pd.read_csv('historical_data.csv')

# Extract hashes and results
historical_hashes = historical_data['Hashes'].values
historical_results = historical_data['Results'].values.astype(float)  # Ensure results are represented as floats

# Convert hashes to numerical features
historical_hashes_numeric = np.array([hash_to_numeric(hash_str) for hash_str in historical_hashes]).reshape(-1, 1)

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
historical_hashes_scaled = scaler.fit_transform(historical_hashes_numeric)

# Create a neural network model
model = Sequential()
model.add(Dense(128, input_dim=1, activation='relu')) # 128 vs 64 neurons?
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5)) # Prevent overfitting
# model.add(Dense(1, activation='linear'))  # Output layer with linear activation for regression
model.add(Dense(1, activation='relu')) # ReLu activation for non-linear regression

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(historical_hashes_scaled, historical_results, epochs=100, batch_size=32, verbose=0)
# history = model.fit(historical_hashes_scaled, historical_results, epochs=100, batch_size=32, verbose=1)
# print("Loss history:", history.history['loss'])

# Function to predict the result of a given hash
def predict_result(hash_input):
    hash_numeric = hash_to_numeric(hash_input)
    hash_scaled = scaler.transform([[hash_numeric]])
    print("Scaled hash input:", hash_scaled)
    predicted_result = model.predict(hash_scaled)
    print("Raw predicted result:", predicted_result)
    return predicted_result[0][0]


# Loop for predicting future hashes
while True:
    user_input_hash = input("Enter the hash (or 'exit' to quit): ")
    
    if user_input_hash.lower() == 'exit':
        print("Exiting the program.")
        break
    
    predicted_output = predict_result(user_input_hash)
    print("Predicted output for the hash", user_input_hash, "is:", predicted_output)
