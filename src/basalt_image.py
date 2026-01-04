# coding:utf-8
#!/usr/bin/python
     
# Extract images from a bag file.
import roslib; #roslib.load_manifest(PKG)
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
     
#Reading bag filename from command line or roslaunch parameter.
#import os
#import sys
     
cam0_path  = '/home/nk/catkin_ws/data/cam0/'     # 已经建立好的存储cam0 文件的目录
cam1_path  = '/home/nk/catkin_ws/data/cam1/'
     
class ImageCreator():
    def __init__(self):
        self.bridge = CvBridge()
        with rosbag.Bag('camera_imu_mocap_1.bag', 'r') as bag:  #要读取的bag文件；
            for topic,msg,t in bag.read_messages():
                if topic == "/camera/infra1/image_rect_raw": #图像的topic；
                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                        except CvBridgeError as e:
                            print (e)
                        timestr = "%.6f" %  msg.header.stamp.to_sec()
                            #%.6f表示小数点后带有6位，可根据精确度需要修改；
                        image_name = timestr+ ".jpg" #图像命名：时间戳.jpg
                        cv2.imwrite(cam0_path + image_name, cv_image)  #保存；
                elif topic == "/camera/infra2/image_rect_raw": #图像的topic；
                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                        except CvBridgeError as e:
                            print (e)
                        timestr = "%.6f" %  msg.header.stamp.to_sec()
                            #%.6f表示小数点后带有6位，可根据精确度需要修改；
                        image_name = timestr+ ".jpg" #图像命名：时间戳.jpg
                        cv2.imwrite(cam1_path + image_name, cv_image)  #保存；
 
     
if __name__ == '__main__':
        #rospy.init_node(PKG)
    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass