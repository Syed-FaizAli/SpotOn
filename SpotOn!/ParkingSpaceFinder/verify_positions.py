import pickle

# Load the parking positions
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

print("Loaded positions:", posList)
