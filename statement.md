Problem Statement

The goal is to provide a **real-time computer vision application** capable of detecting and visually marking **human faces and eyes** within a live video feed from a webcam. This addresses the need for a simple, yet functional, demonstration or foundational tool for basic object detection in image processing.

# Scope of the Project

The project is limited to a single application utilizing the **OpenCV library** and its pre-trained **Haar Cascade classifiers** (`haarcascade_frontalface_default.xml` and `haarcascade_eye.xml`).

* In-Scope:
    * Initialize and capture video from the default system webcam.
    * Convert the video frames to grayscale for efficient processing.
    * Detect human faces and eyes within the live frames.
    * Draw **green rectangles** around detected faces and **blue rectangles** around detected eyes.
    * Display the processed video feed in a window named 'Detector'.
    * Allow the user to quit the application by pressing the 'q' key.
* Out-of-Scope:
    * Storing, saving, or logging any data or video.
    * Implementing advanced tracking, recognition, or deep learning models.
    * Performing detection on pre-recorded videos or static images.
    * User interface elements beyond the main display window.

# Target Users

* **Students and Learners:** Individuals studying **Computer Vision** or **Image Processing** who need a fundamental, working example of face and eye detection using OpenCV.
* **Developers/Engineers:** Those requiring a **quick, boilerplate implementation** of basic object detection for prototyping or as a building block for larger applications.
* **Hobbyists:** Users interested in running simple, real-time computer vision demos on their personal computers.


# High-Level Features

1.  **Real-Time Video Capture:** Initializes and continuously captures frames from the default webcam.
2.  **Face Detection:** Uses the Haar Cascade classifier to detect **frontal human faces** within each video frame and draws a **green bounding box** around them.
3.  **Eye Detection (Region-Specific):** Detects **eyes** but restricts the search to the region of interest (ROI) defined by the detected face, enhancing accuracy and performance. A **blue bounding box** is drawn around the eyes.
4.  **Live Output Display:** Shows the video feed, complete with the drawn detection boxes, in a dedicated window.
5.  **User Exit Control:** Allows the user to gracefully stop the application by pressing 'q'.
