# C++ (hello camera)

A step-by-step walkthrough for creating a C++ project in Visual Studio that acquires images from a camera and measures frame-by-frame pixel differences.

## Getting Started

1. Install Visual Studio
  * A free version (Visual Studio Community 2017) is available: [Download here](https://www.visualstudio.com/downloads/)
      * Make sure you select support for C++
2. Run Visual Studio
3. Create a New project (*File -> New -> Project*)
    * Select a *Visual C++ -> General -> Empty Project* as your template
    * Give the project a name (this will create a project folder) and choose its location
    
You will now have an *empty* Visual C++ project. It contains only the common folder structure and solution/project files, no source code files.

4. Right-click on "Source Files" and Add a new Item, select .cpp file type, and name the file "main.cpp"

**Now you can write some code.**

```c++
//Hello World
#include <iostream>
#include <string>

int main()
{
    std::cout << "Hello World!\n";
    return 0;
}
```

If you prefer, you can also compile this source file directly from the command line. 
[CMD Compile Windows](https://msdn.microsoft.com/en-us/library/ms235639.aspx)

### Setting up VS to use external libraries
We will use the OpenCV library to grab data from a standard webcam and process images.
1. Download OpenCV version 3.3 [OpenCV GitHub](https://github.com/opencv/opencv/releases/tag/3.3.0)
    * Select the *.exe version and run it when it is downloaded. This will self-extract an archive to a location you specify. *Remember this location!*

We must now tell Visual Studio (VS) where the OpenCV libraries (header and binary files) are located.
 * **Important**: We will use the 64-bit version of OpenCV, so switch your VS project build to "x64". 
	* A dropdown menu on the top VS toolbar can be used to select "x64-Debug"

2. Open your VS project's "properties" page(s). You can simply right-click on the name of your project in the *Solution Explorer*
3. Under the "C/C++" property section, add the location of your OpenCV *include* folder in the "Additional Include Directories" field.
     * This location should be: "...\opencv\build\include"

This will tell you VS project where to find the OpenCV header files. You now need to tell it where to find the **binary** files. At compile time, we will use OpenCV's *.lib files.

4. Open your VS project's "properties" page(s).
5. Under the "Linker" property section, select the "General" sub-section. Add the location of your OpenCV library path in the "Additional Library Directories" field.
    * This location should be: "...\opencv\build\x64\vc14\lib"
6. Under the "Linker" property section, select the "Input" sub-section. Add the names of the OpenCV libraries you will use in the "Additional Dependencies" field.
    * Add all of the following: opencv_world330d.lib

**Now you can write some OpenCV code.**

```c++
/* Hello Camera */
#include <iostream> // Include the standard io stream library
#include <string> // Include the strandard string library
#include "opencv2\opencv.hpp" // Include the OpenCV header files

int main(int, char**)
{
    /* Open a video capture stream */
    cv::VideoCapture cap(0); // open the default camera (index 0)
    if (!cap.isOpened()) // check if we succeeded
    {
	    return -1; // return (exit) if we failed
    }
	
    /* Local variables */
    int width = cv::CAP_PROP_FRAME_WIDTH; // store frame width
    int height = cv::CAP_PROP_FRAME_WIDTH; // store frame height
    cv::Mat frame(height, width, CV_8UC3); // make space for the new frame (Note: 3 channels, RGB)
    cv::Mat gray(height, width, CV_8U); // make space for storing the grayscale frame
    cv::Mat previous(height, width, CV_8U); // make space for storing the previous frame
    cv::Mat difference(height, width, CV_8U); // make space for storing the difference frame
    cv::Scalar mean_scalar; // make space for storing the mean value (as OpenCV scalar)
    double mean; // make space for storing the mean value (as double)
    int	framecount = 0; // make a frame counter and initialize to zero

    /* Acquire images from the camera */
    cv::namedWindow("Hello", 1); // create and display a window (with a name)
    std::cout << "Running\n"; // report progress
    while(true)	// loop forever (or until a key is pressed)
    {
        cap >> frame; // get a new frame from camera
        cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY); // convert current frame to grayscale
    
        if (framecount > 0) // check if this is not the first frame
        {
            cv::absdiff(gray, previous, difference); // compute |difference| between previous and current frame pixels
            mean_scalar = cv::mean(difference); // find the mean of all pixel-wise differences
            mean = mean_scalar.val[0]; // extract only the first element from the scalar
            std::cout << mean << "\n"; // print "motion" to terminal
            cv::imshow("Hello", difference); // display result
        }
        previous = gray.clone(); // copy current frame to previous frame
        framecount++; // increment frame counter
        if (cv::waitKey(30) >= 0) break; // check if a key is pressed, if so, break the while loop
    }
    // Note: the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
    }
```

***Build, run, and have fun!***

**Wait!** ...it won't run. *Only* the compiler knows where OpenCV's binary files are located...not your program (executable).
	* The simplest way to fix this is to copy the DLLs (dynamic link libraries, a type of windows binary that links to your executable at run time) to the same folder as your executable. Do that now...copy "opencv_world330d.dll" to your exe's folder. The DLL is found here:
		* "...\opencv\build\x64\vc14\bin"

## Challenge
Write a program in C++ that uses OpenCV to detect the largest RED object in the camera frame and prints the X and Y pixel coordinates of this object's centre to the terminal window.