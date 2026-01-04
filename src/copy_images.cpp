#include <iostream>
#include <fstream>
#include <dirent.h>
#include <vector>
#include <string>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
 
using namespace std;
 
//遍历指定路径下的所有文件，将文件的路径存于vector中
void GetFileNames(string path, vector<string>& filenames)
{
    DIR *pDir;
    struct dirent* ptr;
    if (!(pDir = opendir(path.c_str())))
    {
        cout << "error: Folder doesn't Exist!" << endl;
        return;
    }
    while ((ptr = readdir(pDir))!=0)
    {
        if (strcmp(ptr->d_name, ".") != 0 && strcmp(ptr->d_name, "..") != 0)
        {
            filenames.push_back(ptr->d_name);
        }
    }
    closedir(pDir);
}

 
int main() {
    vector<string> file_names;

    string find = "/home/oywl/multicalib_ws/src/extract_data/src/cam1/";
    string copy = "/home/oywl/multicalib_ws/src/extract_data/src/extract_result4/c-b4/cam0/";
    string paste = "/home/oywl/multicalib_ws/src/extract_data/src/extract_result4/c-b4/cam1/";

    ofstream outFile;
    outFile.open("/home/oywl/multicalib_ws/src/extract_data/src/extract_result4/c-b4/camera_data.csv");

    GetFileNames(copy, file_names);
    sort(file_names.begin(), file_names.end());
    for (int i = 0; i < file_names.size(); i++)
    {
        cout << file_names[i] << endl;
        string image_name = find + file_names[i];
        cv::Mat img = cv::imread(image_name, cv::IMREAD_UNCHANGED);
        cv::imwrite(paste + file_names[i], img);
        string image_time = file_names[i].substr(0, file_names[i].length()-4);
        outFile << image_time << ", " << file_names[i] << endl;
    }
    return 0;
}
