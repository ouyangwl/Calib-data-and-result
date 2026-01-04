#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class ExtractData
{
    public:
    // uint64_t time_offset;
    ofstream outFile;
    ros::Subscriber cam0_sub;
    ros::Subscriber cam1_sub;
    
    ExtractData(string str)
    {
        outFile.open("/home/oywl/multicalib_ws/src/extract_data/src/camera_data.csv");
        ros::NodeHandle nh;
        cam0_sub = nh.subscribe<sensor_msgs::Image>("/camera/infra1/image_rect_raw", 1000, &ExtractData::CameraCallback1, this);
        cam1_sub = nh.subscribe<sensor_msgs::Image>("/camera/infra2/image_rect_raw", 1000, &ExtractData::CameraCallback2, this);
    }

    void CameraCallback1(const sensor_msgs::Image::ConstPtr &msg)
    {
        string nsec;
        string nsec_string = to_string(msg->header.stamp.nsec);
        if( nsec_string.length() == 4)
        {
            nsec = "00000" + nsec_string;
        }
        if( nsec_string.length() == 5)
        {
            nsec = "0000" + nsec_string;
        }
        if( nsec_string.length() == 6)
        {
            nsec = "000" + nsec_string;
        }
        if( nsec_string.length() == 7)
        {
            nsec = "00" + nsec_string;
        }
        if( nsec_string.length() == 8)
        {
            nsec = "0" + nsec_string;
        }
        if( nsec_string.length() == 9)
        {
            nsec = nsec_string; 
        }

        string image_time = to_string(msg->header.stamp.sec) + nsec;
        // std::cout << image_time <<std::endl;

        string cam0 = "/home/oywl/multicalib_ws/src/extract_data/src/cam0/";

        cv_bridge::CvImagePtr cv_ptr;
        cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
        string image_name = cam0 + image_time + ".jpg";
        cv::imwrite(image_name, cv_ptr->image);

        outFile << image_time << ", " << string(image_time) + ".jpg" << endl;
    }

    void CameraCallback2(const sensor_msgs::Image::ConstPtr &msg)
    {
        string nsec;
        string nsec_string = to_string(msg->header.stamp.nsec);
        if( nsec_string.length() == 5)
        {
            nsec = "0000" + nsec_string;
        }
        if( nsec_string.length() == 6)
        {
            nsec = "000" + nsec_string;
        }
        if( nsec_string.length() == 7)
        {
            nsec = "00" + nsec_string;
        }
        if( nsec_string.length() == 8)
        {
            nsec = "0" + nsec_string;
        }
        if( nsec_string.length() == 9)
        {
            nsec = nsec_string; 
        }

        string image_time = to_string(msg->header.stamp.sec) + nsec;

        string cam1 = "/home/oywl/multicalib_ws/src/extract_data/src/cam1/";

        cv_bridge::CvImagePtr cv_ptr;
        cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
        string image_name = cam1 + image_time + ".jpg";
        cv::imwrite(image_name, cv_ptr->image);
  
    }

    ~ExtractData()
    {
        outFile.close();
    }
};

 
int main(int argc, char **argv)
{
    ros::init(argc, argv, "extract_camera_data");
    ExtractData extract_data("extract_camera_data");
    ros::spin();
    return 0;
}
