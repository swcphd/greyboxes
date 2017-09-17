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
	while (true)	// loop forever (or until a key is pressed)
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
// FIN