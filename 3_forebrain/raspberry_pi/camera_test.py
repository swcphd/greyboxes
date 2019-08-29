import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera() # PiCamera object
camera.resolution = (640, 480)
camera.framerate = 32
frame = PiRGBArray(camera) # PiRGBArray object
time.sleep(0.1) # 100ms

running = True
while running:
    # capture frames from the camera
    for frame in camera.capture_continuous(frame, format="bgr", use_video_port=True):
        # store the array attribute of the frame object
        image = frame.array

        # show the frame
        cv2.imshow("picam", image)
        # waits 1ms for a key event, masks everything except the least significant byte
        key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        frame.truncate(0)

        # if the `q` key was pressed,
        # break out of the for and exit the while
        if key == ord("q"):
            break
    running = False
cv2.destroyAllWindows()