#include "ros/ros.h" 
/*which includes:
    #include "ros/time.h"
    #include "ros/rate.h"
    #include "ros/init.h"
    #include "ros/node_handle.h"
    ...
*/

#include "std_msgs/Header.h"
#include "std_msgs/String.h"


#include "darknet_ros_msgs/BoundingBox.h"
#include "darknet_ros_msgs/BoundingBoxes.h"


using namespace darknet_ros_msgs;
using namespace std;

std_msgs::String msg_command;
BoundingBox cv_output;
BoundingBoxes cv_output_list;
bool tracking_en = 0;
int saved_index = 0;
int resolution_x = 640;
int resolution_y = 480;
int tolerance_x = 60;
int lower_x = (resolution_x - tolerance_x)/2;
int upper_x = (resolution_x + tolerance_x)/2;

//-------------         Return the key      -------------//
void CV_OUTPUT(const BoundingBoxes& msg)
{
    cv_output_list = msg;
}


int main(int argc, char **argv)
{
    //-------------         Initialization      -------------//
    ros::init(argc, argv, "Manual_Control_Controller");
    ros::NodeHandle n;

    //-------------         Topics              -------------//
    ros::Subscriber sub_key_down = n.subscribe("/CV_output", 1000, CV_OUTPUT);
    ros::Publisher command_pub = n.advertise<std_msgs::String>("/jetbot_motors/cmd_str", 1000);

    //-------------         ROS Spinner         -------------//
    ros::AsyncSpinner spinner(2);
    spinner.start();

    //-------------         Control Loop         -------------//
    ros::Rate loop_rate(20);
    msg_command.data = "stop";
    while (ros::ok())
    {
        tracking_en = 0;
        cout << "elements: " << cv_output_list.bounding_boxes.size() << endl;

        if (cv_output_list.bounding_boxes.size() != 0)
        {
            for (auto i = 0; i< cv_output_list.bounding_boxes.size(); i++)
            {
                if (cv_output_list.bounding_boxes[i].Class == "person")
                {
                    tracking_en = 1;
                    cv_output = cv_output_list.bounding_boxes[i];
                    break;
                }
                else tracking_en = 0;
            }
        }
        else tracking_en = 0;
        
        
        if (tracking_en == 1)
        {
            
            int center_location_x = (cv_output.xmin + cv_output.xmax)/2;

            cout << "xmin: " << cv_output.xmin << endl;
            cout << "xmax: " << cv_output.xmax << endl;
            cout << "Center: " << center_location_x << endl;

            if((center_location_x >= lower_x) && (center_location_x <= upper_x)) msg_command.data = "forward";
            else if (center_location_x < lower_x) msg_command.data = "left";
            else if (center_location_x > lower_x) msg_command.data = "right";
            else msg_command.data = "stop";
        }
        else msg_command.data = "stop";


        command_pub.publish(msg_command);     
        loop_rate.sleep();
    }
    return 0;
}

/*
ROS Headers:    http://docs.ros.org/en/indigo/api/roscpp/html/ros_8h.html 
jetbot_ros:     https://www.hackster.io/belochka/controlling-the-jetbot-robot-from-ros-014620 
                https://github.com/dusty-nv/jetbot_ros 
Keyboard:       https://github.com/ros-teleop/teleop_twist_keyboard 
                https://github.com/lrse/ros-keyboard 
Useful Later:   https://stackoverflow.com/questions/71808245/ros-subscriber-undefined-reference 
Experiences:    #1  If there is none in parameter of callback functions, ERROR
                #2  Cannot PUBLISH std::String, publish std_msgs::String instead: https://answers.ros.org/question/256448/why-cant-i-send-a-string-message-through-my-program/ 
*/