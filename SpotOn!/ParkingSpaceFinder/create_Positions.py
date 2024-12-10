import pickle

# Sample parking positions (replace with actual positions)
posList = [
    (50, 50), (150, 50), (250, 50),
    (50, 150), (150, 150), (250, 150),
    (50, 250), (150, 250), (250, 250)
]

# Save the positions to a file named 'CarParkPos'
with open('CarParkPos', 'wb') as f:
    pickle.dump(posList, f)

print("CarParkPos file created successfully.")
