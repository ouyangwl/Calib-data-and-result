#include <ros/ros.h>
#include <sensor_msgs/Imu.h>
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
        outFile.open("/home/oywl/multicalib_ws/src/extract_data/src/imu_data.csv");
        outFile << "#timestamp [ns], w_x [rad s^-1], w_y [rad s^-1], w_z [rad s^-1], a_x [m s^-2], a_y [m s^-2], a_z [m s^-2]" << endl;
        ros::NodeHandle nh;
        rpy_sub = nh.subscribe<sensor_msgs::Imu>("/imu/data", 1000, &ExtractData::IMUCallback, this);
    }

    void IMUCallback(const sensor_msgs::Imu::ConstPtr &msg)
    {
        string nsec;
        string nsec_string = to_string(msg->header.stamp.nsec);
        if( nsec_string.length() == 3)
        {
            nsec = "000000" + nsec_string;
        }
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
                << setprecision(10) << msg->angular_velocity.x << ", "
                << setprecision(10) << msg->angular_velocity.y << ", "
                << setprecision(10) << msg->angular_velocity.z << ", "
                << setprecision(10) << msg->linear_acceleration.x << ", "
                << setprecision(10) << msg->linear_acceleration.y << ", "
                << setprecision(10) << msg->linear_acceleration.z << endl;    
    }

    ~ExtractData()
    {
        outFile.close();
    }
};

 
int main(int argc, char **argv)
{
    ros::init(argc, argv, "extract_imu_data");
    ExtractData extract_data("extract_imu_data");
    ros::spin();
    return 0;
}
