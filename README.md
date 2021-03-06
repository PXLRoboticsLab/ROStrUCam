# ROStrUCam
ROS Stream USB Camera: a simple ROS node to stream standard USB Camera's.

## Getting started
You can follow the instructions below to deploy this project to your local machine.

### Prerequisites
For this project to work you first need to install some dependencies. 

* OpenCV 3
* ROS (Indigo or newer)

### Install
Follow the steps below to install and run the project locally:
1. Clone this repository into your catkin_ws: `$ git clone https://github.com/PXLRoboticsLab/ROStrUCam.git`
2. Give the script run permission: `$ sudo chmod u+x connect.py`
3. Start a roscore: `$ roscore`
4. Run the script: `$ rosrun ROStrUCam connect.py [--index] [--topic] [--fps] [--width] [--height] [--screen]`:
	* --index (**int**): The index of the usb camera, most of the time this is 0 unless you have an internal camera and want to use an external USB camera.
	* --topic (**String**): The name of the ROS topic you want to publish to.
	* --fps (**int**): The maximum amount of frames to publish per second.
	* --width (**int**): The width of the camera stream.
	* --height (**int**): The height of the camera stream.
	* --screen (**stores_true**): Show a GUI with the camera stream.

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/PXLRoboticsLab/ROStrUCam/blob/master/LICENSE.md)  file for details.

## Authors
* [Maarten Bloemen](https://github.com/MaartenBloemen) 
