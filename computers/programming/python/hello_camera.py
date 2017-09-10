# -*- coding: utf-8 -*-
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
camera = 1

# Specifiy number of frames to acquire
num_frames = 100

# Open camera stream
cam = cv2.VideoCapture(camera)

# Get image size
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Make space for intermediate images (or correct data type)
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
       print("Start...\n")
              
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

# FIN
