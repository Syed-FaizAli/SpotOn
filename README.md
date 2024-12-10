# SpotOn!
A Parking Space Finder Project
Parking Spot Finder

Overview

The Parking Spot Finder is a computer vision-based application designed to monitor and detect available parking spaces in a parking lot using video footage. This project processes video input and dynamically identifies free and occupied parking spots, displaying the results in real-time on the video feed. It serves as a working prototype to demonstrate the feasibility of automated parking spot detection.

Features

Real-time detection of free and occupied parking spots.

Visual overlay of parking spot status (green for free, red for occupied) on the video feed.

Display of the total count of available parking spaces.

Configurable parking spot dimensions and detection thresholds.

How It Works

Input: A video feed of the parking lot (e.g., carPark.mp4).

Preprocessing: The video frames are preprocessed using techniques like grayscale conversion, Gaussian blurring, thresholding, and dilation to isolate parking spots.

Detection: Each parking spot is analyzed to determine its status (free or occupied) based on pixel intensity thresholds.

Output: The processed video displays the parking spots with color-coded rectangles and the count of free spaces.

Prerequisites

Python 3.x

Required Python libraries:

OpenCV

Numpy

cvzone

pickle

Installation

Clone the repository or download the project files.

Install the required Python libraries using pip:

pip install opencv-python numpy cvzone

Ensure that the following files are present in the project directory:

main.py (the main program script)

carPark.mp4 (sample video of the parking lot)

CarParkPos (file containing parking spot coordinates, serialized using pickle)

IMAGE.png (optional overlay image for debugging purposes)

Usage

Run the script using Python:

python main.py

The video feed will open in a new window, displaying parking spots with a real-time count of available spaces.

To exit the program, press the q key.

Configuration

Parking Spot Dimensions: Modify the width and height variables in main.py to match the size of parking spaces in your video.

Detection Threshold: Adjust the threshold value in the checkParkingSpace function to fine-tune the sensitivity of the detection algorithm.

Limitations

The current implementation is a working prototype and may require further calibration for different lighting conditions, camera angles, and parking lot layouts.

The CarParkPos file must contain accurate parking spot coordinates for correct detection.

Performance may vary depending on video resolution and processing power.

Future Improvements

Integration with live camera feeds.

Enhanced robustness to varying lighting and weather conditions.

Machine learning models for more accurate and adaptive parking spot detection.

Support for multi-level parking structures.

Acknowledgments

This project was built using OpenCV and inspired by the need for smarter parking solutions. Special thanks to the open-source community for their valuable tools and libraries.

Feel free to contribute or provide feedback to improve this prototype!

