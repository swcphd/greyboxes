# Python (hello camera)

A step-by-step walkthrough for creating a Python script in Anaconda/Spyder that uses OpenCV to acquire images from a camera and measure frame-by-frame pixel differences.

## Getting Started

1. Install Anaconda 
  * [Download Anaconda](https://www.anaconda.com/download/)
    * Get the latest version (4.4.0 with Python 3.6, 64-bit)
2. Open Spyder (Scientific Python Development Environment)
	* This is one of the IDEs installed with Anaconda. It has many tools convenient for "scientific python"
	* You can launch Spyder by first launching the "Anaconda Navigator" or searching for it in the Windows search box
		* It is useful to add a desktop shortcut or pin Spyder to your task bar
3. Create a new python script (just type into the *Editor* window)
```python
# Hello World
print('Hello, world!')
```
Python scripts are "run" in the interpreter by sending each command in the order they appear. You can also just type a sequence of commands into the intepreter directly, but scripts are far more convenient.

4. Run your first Python script (Select Run -> Run) or just press F5

### Setting up Python to use external libraries
We will use the OpenCV library to grab data from a standard webcam and process images.

Many common packages are installed with Anaconda, but the latest version of OpenCV is not. You will have to install it yourself.
  * Go here: [Windows Binaries for Python](http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv)
    * Download: **opencv_python-3.3.0-cp36-cp36m-win_amd64.whl**
      * or "with contrib"

The WHL file contains everything you need to install the OpenCV python library.
  * Open an *Anaconda Prompt*, go to the directory with the WHL file and run:
```
pip install opencv_python-3.3.0-cp36-cp36m-win_amd64.whl
```

OpenCV should now be installed in your Python distribution. To test this, restart Spyder and run the follwing command.
```python
import cv2
```
If this command does not reply with an error (e.g. "Module Not Found"), then you are ready to go.
	* *Note:* You may get an error that a "numpy.core..." module was the wrong version. This means that your version of OpenCV requires a more recent version of NumPy than the one installed by Anaconda. You can "upgrade" your NumPy to the latest version by running the following command at the Anaconda prompt, and then restarting Spyder.
```
pip install numpy --upgrade
```

**Now you can write some OpenCV Python code.**

```python
"""
Hello Camera example in Python (using opencv)
"""
# Import useful libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import time

# Specify camera/device number (usually 0)
camera = 0

# Specifiy number of frames to acquire
num_frames = 100

# Open camera stream
cam = cv2.VideoCapture(camera)

# Get image size
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Make space for intermediate images (of correct data type)
gray = np.zeros((height, width), dtype = np.uint8)
gray_float = np.zeros((height, width), dtype = np.float32)
previous = np.zeros((height, width), dtype = np.float32)
difference = np.zeros((height, width), dtype = np.float32)

# Acquire frames, measure change from previous frame
for i in range(0, num_frames):
    
    # Read the next image from camera
    ret_val, image = cam.read()

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert to floating-point
    gray_float = np.float32(gray)
    
    # Ignore first image
    if (i == 0):
       print("Running\n")              
    else:
        # Subtract previous image
        difference = np.abs(gray_float-previous)
        
        # Average all pixel differences
        average = np.mean(np.mean(difference))
        print(average)
        
    # Store previous frame
    previous = np.copy(gray)
    
# Release the camera "handle"
cam.release()
```

***Run and have fun!***

## Challenge
Write a program in Python that uses OpenCV to detect the largest RED object in the camera frame and prints the X and Y pixel coordinates of this object's centre to the terminal window.