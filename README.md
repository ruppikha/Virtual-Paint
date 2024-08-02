# Virtual-Paint
Color Detection and Tracking

This project implements a basic color detection and tracking system using OpenCV in Python. The code captures video input from a webcam, detects specified colors (blue and green), and tracks the detected colors by drawing circles on the live video feed.

Requirements

Python 3.x
OpenCV library
NumPy library
You can install the required libraries using pip:

bash
Copy code
pip install opencv-python numpy
Usage

Clone the repository or download the code.
Run the Python script:
bash
Copy code
python color_detection.py
Ensure your webcam is connected. The script will try to open the video device, and if successful, it will start capturing video.
Press 'q' to quit the video feed.
Code Explanation

Variables
frameWidth and frameHeight: Set the width and height of the video frame.
myColors: List of HSV color ranges to detect. Each color is represented by six values [H_min, S_min, V_min, H_max, S_max, V_max].
myColorValues: List of BGR values for drawing detected colors on the image.
myPoints: List to store detected points [x, y, colorId].
Functions
findColor(img, myColors, myColorValues): Converts the input image to HSV, creates masks for specified colors, finds contours, and detects colors.
getContours(img): Finds contours in the mask and returns the center coordinates of the largest contour.
drawOnCanvas(myPoints, myColorValues): Draws circles on the image at detected points.
Main Loop
Capture a frame from the webcam.
Call findColor to detect specified colors in the frame.
Extend myPoints with new detected points.
Draw detected points on the frame using drawOnCanvas.
Display the result.
Exit the loop and close the window when 'q' is pressed.
Color Detection Flags
Flags are used to indicate whether a specific color has been detected. Text messages are displayed on the video feed for detected colors.

Notes

The color ranges in myColors are set for blue and green colors. Adjust the HSV values to detect different colors.
The script displays individual masks for each color for debugging purposes.
The contour area threshold is set to 500. Adjust this value based on your requirements.
Example Output

The script displays the live video feed with detected colors marked by circles. If blue or green colors are detected, text messages "Blue detected" or "Green detected" are displayed on the video feed.

Troubleshooting

If the video device cannot be opened, ensure your webcam is connected and working.
Adjust the HSV values in myColors to better match the colors you want to detect.
Increase or decrease the contour area threshold in getContours if the script is not detecting the colors correctly.

