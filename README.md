Kalman Filter for Noisy GPS Trajectory – Beijing Taxi Data (2008)
This project uses a Kalman Filter to clean up noisy GPS data from a taxi in Beijing. 
It shows how we can take messy, real-world GPS points and make them smoother and easier to understand.


📁 Dataset
Source: Microsoft Research Asia – GPS Trajectories
Used file: 1.txt
Columns: Taxi_ID; Timestamp; Longitude; Latitude


🧠 What is a Kalman Filter?
A Kalman Filter is like a smart guesser. It keeps guessing where the taxi should be next, then checks the actual GPS reading, and adjusts its guess 
to get closer to reality over time.


⚙️ How It Works
It assumes the taxi moves with nearly constant speed.
For each new GPS point:
1. It makes a prediction.
2. Then it sees the real GPS reading.
3. It adjusts the guess based on accuracy
4. It repeats this again and again for every point.


📊 What You’ll See
The original GPS path (raw data) looks jumpy and messy.
The Kalman Filter path is smooth and more realistic.


Sample image of results below:
<img width="1055" height="739" alt="image" src="https://github.com/user-attachments/assets/13b53b75-bd32-4207-bf19-716e8536ff32" />
<img width="1298" height="736" alt="image" src="https://github.com/user-attachments/assets/b5119c2e-2c5f-4d00-a5ad-6ba1962c0740" />



📦 Files in This Repo
File	What it does
taxi_kalman_filter.py	Python script with Kalman code
Kalman_filter_sim.ipynb	Notebook with step-by-step example
1.txt	-> Real GPS data of a Beijing taxi
filtered_output.png -> Output image of filtered GPS path
README.md	You're reading it!


🛠 Tools Used
Python
Libraries: numpy, pandas, matplotlib, filterpy
Kalman Filter (2D, for GPS smoothing)


Dataset Source: https://www.microsoft.com/en-us/research/publication/t-drive-trajectory-data-sample/
T-Drive Trajectory Data Sample
Provided by: Yu Zheng, Microsoft Research Asia, August 2011.
