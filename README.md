# AI-ML-Project-25BCY10217
Real-Time Face and Eye Detection

# Overview of the Project

This project implements a real-time object detection system using Python and OpenCV to identify human faces and eyes within a live webcam feed. It utilizes the pre-trained Haar Cascade classifiers for fast and efficient detection, making it suitable for simple computer vision applications that require identifying facial features.

The application captures video from the default camera, processes each frame, and draws bounding boxes around the detected objects: faces are marked with green rectangles, and eyes are marked with blue rectangles within the face region.

# Features

Real-Time Processing: Captures and processes video frames from the webcam in real time.

Face Detection: Accurately detects and outlines the primary face region using the haarcascade_frontalface_default.xml classifier.

Eye Detection: Detects eyes within the boundaries of the detected face, leveraging the haarcascade_eye.xml classifier for improved performance and accuracy.

Visual Feedback: Draws distinct bounding boxes (green for face, blue for eyes) for immediate visual confirmation.

Simple Control: Allows the user to exit the application by pressing the 'q' key.

# Technologies/Tools Used

Technology -Role

Python-The core programming language used for the application logic.

OpenCV (cv2)-The primary library for computer vision tasks, including video capture, image processing, and detection algorithms.

Haar Cascades-Pre-trained models (haarcascade_frontalface_default.xml and haarcascade_eye.xml) used for object detection.

# Steps to Install & Run the Project

Follow these steps to set up and run the face and eye detection application on your local machine.

Prerequisites

You must have Python installed on your system.

Installation

Clone the repository:

git clone https://github.com/aryaman180578/AI-ML-Project-25BCY10217/tree/main
cd AI-ML-Project-25BCY10217


Install the required library (OpenCV):

pip install opencv-python


Note: OpenCV automatically includes the necessary Haar Cascade XML files, which your script uses via cv2.data.haarcascades.

Save the code:
Save the provided Python code into a file named, for example, detector.py.

# Running the Project

Run the Python script from your terminal:

python detector.py


A new window titled "Detector" will open, displaying the live video feed from your webcam with the bounding boxes drawn around faces and eyes.

# Instructions for Testing

Start the application using the command python detector.py.

Ensure your webcam is active (the "Detector" window should show a live feed).

Position your face in front of the camera.

# Observe the results:

A green rectangle should appear around your entire face.

Blue rectangles should appear around your eyes (within the green face rectangle).

Move around or introduce another person to test the system's ability to track movement and detect multiple faces.

To stop the application, focus on the "Detector" window and press the q key on your keyboard.
