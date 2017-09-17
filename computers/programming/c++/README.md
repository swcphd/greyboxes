# C++ (hello camera)

A step-by-step walkthrough of creating a C++ project in Visual Studio that acquires images from a camera and measures motion.

## Getting Started

* Install Visual Studio (Viusal Studio Community 2017). Make sure you install support for C++.
* Open Visual Studio
* Create a New project
* Select Visual C++ - Win32 - Console application as your template
* Give the project a name (this will create a project folder) and choose its location
* On the pop-up window, click "Next" and then check the box next to "Empty Project"
* Click Finish

You will now have an empty Visual C++ project. It contains only the common folder structure and project files, no source code files.

* Right-click on "Source Files" and Add a new Item, select .cpp file type, and name the file "main.cpp"

Now you can write some code.

```c++
//Hello World
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main()
{
    std::cout << "Hello World!" << endl;
    return 0;
}
```

If you prefer, you can also compile this source fiel directly from the command line. 
[CMD Compile Windows](https://msdn.microsoft.com/en-us/library/ms235639.aspx)


We will use the OpenCV library to grab data from a standard webcam and process images.
1. Download OpenCV version 3.3 [OpenCV GitHub](https://github.com/opencv/opencv/releases/tag/3.3.0)
 * Select the *.exe version and run it. This will self-extract an archive to a location you specify. Remember this location!

We must now tell Visual Studio (VS) where the OpenCV libraries are located.
**Important**: We will use the 64-bit version of OpenCV, so switch your VS project build to "x64".

2. Open your VS project "properies" page(s). You can simply right-click on the name of your project.
3. Under the "C/C++" property section, add the location of your OpenCV include path in the "Additional Include Directories" field.
 * This location should be: "...\opencv\build\include"

This will tell you VS project where to find the OpenCV header files. You now need to tell it where to find the binary files.
4. Open your VS project "properies" page(s).
5. Under the "Linker" property section, select the "General" sub-section. Add the location of your OpenCV library path in the "Additional Library Directories" field.
 * This location should be: "...\opencv\build\x64\vc14\lib"
6. Under the "Linker" property section, select the "Input" sub-section. Add the names of the OpenCV libraries you will use in the "Additional Dependencies" field.
 * Add all of the following: opencv_world330d.lib

```c++
// Hello Camera
#include <iostream>
#include <string>
#include <vector>

#include "opencv2\opencv.hpp"


using namespace cv;

int main(int, char**)
{
	VideoCapture cap(0); // open the default camera
	if (!cap.isOpened())  // check if we succeeded
		return -1;

	Mat edges;
	namedWindow("edges", 1);
	for (;;)
	{
		Mat frame;
		cap >> frame; // get a new frame from camera
		cvtColor(frame, edges, COLOR_BGR2GRAY);
		GaussianBlur(edges, edges, Size(7, 7), 1.5, 1.5);
		Canny(edges, edges, 0, 30, 3);
		imshow("edges", edges);
		if (waitKey(30) >= 0) break;
	}
	// the camera will be deinitialized automatically in VideoCapture destructor
	return 0;
}
```

Build, run, and have fun!

Wait...it won't run because only the compiler knows where OpenCV is...not your program. The simplest way to fix this is to copy the DLLs you use to the same folder as your executable. Do that....copy "opencv_world330d.dll" to your exe's folder. The DLL
