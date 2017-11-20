#!/usr/bin/env python
import cv2
from sensor_msgs.msg import Image
import rospy
from cv_bridge import CvBridge, CvBridgeError
import argparse


class Connect:
    def __init__(self, args):

        vc = cv2.VideoCapture(args.index)
        vc.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
        vc.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)

        image_pub = rospy.Publisher(args.topic, Image, queue_size=args.fps)
        rate = rospy.Rate(args.fps)
        bridge = CvBridge()

        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False

        print('Opening 360 camera stream.')
        while not rospy.is_shutdown() and rval:
            try:
                rosImg = bridge.cv2_to_imgmsg(frame, 'bgr8')
            except CvBridgeError as error:
                print(error)
            image_pub.publish(rosImg)
            if args.screen:
                cv2.imshow('360 cam stream', frame)
            if cv2.waitKey(1) == 27:
                exit(0)
            rval, frame = vc.read()
            rate.sleep()


if __name__ == '__main__':
    rospy.init_node('pixpro_connector')
    parser = argparse.ArgumentParser()

    parser.add_argument('--index', type=int,
                        help='Index of the usb camera.', default=0)
    parser.add_argument('--topic', type=str,
                        help='The name of the rostopic.', default="focus_vision/image/compressed")
    parser.add_argument('--fps', type=int,
                        help='The max frame rate of the camera.', default=30)
    parser.add_argument('--width', type=int,
                        help='The width of the stream.', default=1440)
    parser.add_argument('--height', type=int,
                        help='The height of the stream.', default=720)
    parser.add_argument('--screen', action='store_true',
                        help='Show a GUI of the camera stream.')
    args = parser.parse_args()
    Connect(args)