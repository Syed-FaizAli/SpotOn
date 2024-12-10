import cv2
import pickle
import cvzone
import numpy as np
import os

# Video feed
cap = cv2.VideoCapture('carPark.mp4')

# Load the parking positions
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

# Path to the overlay image
overlay_path = 'IMAGE.png'

# Check if the overlay image exists
if not os.path.isfile(overlay_path):
    print(f"File {overlay_path} not found. Please check the file path.")
    exit()

# Load the overlay image
overlay_img = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)

if overlay_img is None:
    print("Failed to load the overlay image. Please check the file path and format.")
    exit()

print("Overlay image successfully loaded.")

# Set the width and height for the parking space rectangles
width, height = 27, 60

# Create the window before the loop
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

# Function to check parking space
def checkParkingSpace(imgPro, debug=False):
    spaceCounter = 0
    for pos in posList:
        x, y = pos
        
        # Ensure the crop is within image bounds
        if y + height <= imgPro.shape[0] and x + width <= imgPro.shape[1]:
            imgCrop = imgPro[y:y + height, x:x + width]
            count = cv2.countNonZero(imgCrop)
            
            # Adjust threshold dynamically (change this as needed)
            threshold = 500
            if count < threshold:  # Spot is empty
                color = (0, 255, 0)  # Green for available
                thickness = 5
                spaceCounter += 1
            else:
                color = (0, 0, 255)  # Red for occupied
                thickness = 2

            # Draw rectangle and count value
            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
            cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0, colorR=color)
            
            # Debugging: Print count values for each spot
            if debug:
                print(f"Spot ({x}, {y}) Count: {count}")
        else:
            print(f"Skipping spot at ({x}, {y}) - out of bounds")
    
    # Display the total count
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3, thickness=5, offset=20, colorR=(0, 200, 0))

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()

    if not success:
        break

    # Preprocess the image
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)

    # Advanced preprocessing with Canny edge detection
    imgCanny = cv2.Canny(imgGray, 50, 150)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgCanny, kernel, iterations=1)

    # Combine preprocessing methods
    imgFinal = cv2.bitwise_or(imgDilate, imgMedian)

    # Check parking spaces with debugging enabled
    checkParkingSpace(imgFinal, debug=True)

    # Display the result
    cv2.imshow("Image", img)

    # Exit when 'q' is pressed
    if cv2.waitKey(132) & 0xFF == ord('q'):
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()