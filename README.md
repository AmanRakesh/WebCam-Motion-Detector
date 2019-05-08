# WebCam-Motion-Detector
This will detect any motion in front of webcam and then generate a graph which will show time analysis of activities in front of it.

Run the plotting.py file it will automaically activate the motionDetect file. It will open four windows capturing video in normal, greyscale, threshold form and delta form.

Any motion will be detected inside the normal window with a square that will follow the actions of user. 
After capturing the start and end time of the motions that occured in front of webcam it will make csv file which will contain data about start and end of any motion.

To Quit from the video Capture window press 'q' and then wait for 2 seconds.

Finally the plotting.py file will generate a html file which will show the graph, which will tell about when the motion started and ended.
Just hover the plot to get more details of Time analysis.
