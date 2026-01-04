#include <ros/ros.h>
#include <nav_msgs/Odometry.h>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class ExtractData
{
    public:
    // uint64_t time_offset;
    ofstream outFile;
    ros::Subscriber rpy_sub;
    
    ExtractData(string str)
    {
        outFile.open("/home/oywl/slam_ws/openvins_ws/src/result/groundtruth.txt");
        outFile << "# timestamp(s) tx ty tz qx qy qz qw" << endl;
        ros::NodeHandle nh;
        rpy_sub = nh.subscribe<nav_msgs::Odometry>("/odom", 1000, &ExtractData::OdomCallback, this);
    }

    void OdomCallback(const nav_msgs::Odometry::ConstPtr &msg)
    {
        outFile << msg->header.stamp << " "
                << msg->pose.pose.position.x << " "
                << msg->pose.pose.position.y << " "
                << msg->pose.pose.position.z << " "
                << msg->pose.pose.orientation.x << " "
                << msg->pose.pose.orientation.y << " "
                << msg->pose.pose.orientation.z << " "
                << msg->pose.pose.orientation.w << endl;    
    }

    ~ExtractData()
    {
        outFile.close();
    }
};

 
int main(int argc, char **argv)
{
    ros::init(argc, argv, "extract_gt_data");
    ExtractData extract_data("extract_gt_data");
    ros::spin();
    return 0;
}
