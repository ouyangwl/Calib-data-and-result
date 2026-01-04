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
        outFile.open("/home/oywl/multicalib_ws/src/extract_data/src/mocap_data.csv");
        outFile << "#timestamp [ns], p_x [m], p_y [m], p_z [m], q_x [], q_y [], q_z [], q_w [], v_x [], v_y [], v_z [], rv_x [], rv_y [], rv_z []" << endl;
        ros::NodeHandle nh;
        rpy_sub = nh.subscribe<nav_msgs::Odometry>("/odom", 1000, &ExtractData::OdomCallback, this);
    }

    void OdomCallback(const nav_msgs::Odometry::ConstPtr &msg)
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

        outFile << msg->header.stamp.sec << nsec << ", "
                << setprecision(10) << msg->pose.pose.position.x << ", "
                << setprecision(10) << msg->pose.pose.position.y << ", "
                << setprecision(10) << msg->pose.pose.position.z << ", "
                << setprecision(10) << msg->pose.pose.orientation.x << ", "
                << setprecision(10) << msg->pose.pose.orientation.y << ", "
                << setprecision(10) << msg->pose.pose.orientation.z << ", "
                << setprecision(10) << msg->pose.pose.orientation.w << ", "
                << setprecision(10) << msg->twist.twist.linear.x << ", "
                << setprecision(10) << msg->twist.twist.linear.y << ", "
                << setprecision(10) << msg->twist.twist.linear.z << ", "
                << setprecision(10) << msg->twist.twist.angular.x << ", "
                << setprecision(10) << msg->twist.twist.angular.y << ", "
                << setprecision(10) << msg->twist.twist.angular.z << endl;    
    }

    ~ExtractData()
    {
        outFile.close();
    }
};

 
int main(int argc, char **argv)
{
    ros::init(argc, argv, "extract_mocap_data");
    ExtractData extract_data("extract_mocap_data");
    ros::spin();
    return 0;
}
