# Opencv-Real-Time-Face-Detector
## Prerequisites:
- [OpenCV](https://opencv.org/releases/)
- [Python 3.7.5](https://www.python.org/downloads/release/python-375/)
- [CMake](https://cmake.org/download/)
- [dlib library](http://dlib.net/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
## Process: 
In this repo, I used Haar feature-based cascade classifiers which has a pre-trained machine learning functions that detect faces and other objects in an effective manner.
First capturing the video through a webcam, then converting each frame from the video to gray-scale image, so that the cascade classifier can work faster in detecting faces.

Before Running the [face_detector.py](https://github.com/siudro/Opencv-Real-Time-Face-Detector/blob/main/face_detector.py) file, first create a virtual environment and add the python file into it, then make sure to modify the directory in [line 3](
https://github.com/siudro/Opencv-Real-Time-Face-Detector/blob/ccdb000187b48ff22f4215194a7b620bbe7ad39f/face_detector.py#L3)
to the exact directory where you saved the [haarcascade_frontalface_default.xml](https://github.com/siudro/Opencv-Real-Time-Face-Detector/blob/main/haarcascade_frontalface_default.xml) file.
