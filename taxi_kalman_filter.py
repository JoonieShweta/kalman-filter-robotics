import os
# List all files and folders in the current directory
print("📁 Current Directory Contents:")
for item in os.listdir():
    print("—", item)
release_path = "release"
print(f"📁 Contents of folder: {release_path}")
for item in os.listdir(release_path):
    print("—", item)
data_folder = "release/taxi_log_2008_by_id"
print(f"📁 Contents of: {data_folder}")
for item in os.listdir(data_folder):
    print("—", item)
import pandas as pd

# Define the path to the file
file_path = "release/taxi_log_2008_by_id/1.txt"

# Read the file into a DataFrame
df = pd.read_csv(file_path, header=None, names=["Taxi_ID", "Timestamp", "Longitude", "Latitude"])

# Display the first few rows
df.head()
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.plot(df["Longitude"], df["Latitude"], 'o-', label="Raw GPS", color='red', alpha=0.6)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Raw Taxi Trajectory")
plt.legend()
plt.grid(True)
plt.show()
import numpy as np

# Prepare measurement data
measurements = np.vstack((df["Longitude"].values, df["Latitude"].values)).T

# Initialize Kalman Filter parameters
n = len(measurements)
predicted = []
x = np.array([[measurements[0, 0]], [measurements[0, 1]]])  # initial state (position)
P = np.eye(2) * 1000  # initial uncertainty
F = np.eye(2)         # state transition matrix
H = np.eye(2)         # measurement function
R = np.eye(2) * 0.0001  # measurement noise
Q = np.eye(2) * 0.00001  # process noise

# Kalman Filter loop
for z in measurements:
    # Prediction
    x = F @ x
    P = F @ P @ F.T + Q

    # Update
    Z = np.array([[z[0]], [z[1]]])
    y = Z - H @ x
    S = H @ P @ H.T + R
    K = P @ H.T @ np.linalg.inv(S)
    x = x + K @ y
    P = (np.eye(2) - K @ H) @ P

    predicted.append(x.flatten())

predicted = np.array(predicted)
plt.figure(figsize=(10, 6))

# Raw trajectory
plt.plot(df["Longitude"], df["Latitude"], 'ro-', label='Raw GPS', alpha=0.4)

# Kalman filtered trajectory
plt.plot(predicted[:, 0], predicted[:, 1], 'bo-', label='Kalman Filtered', alpha=0.8)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Taxi Trajectory: Raw vs. Kalman Filtered")
plt.legend()
plt.grid(True)
plt.show()
