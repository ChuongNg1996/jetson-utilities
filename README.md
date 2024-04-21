# Jetson Utilities
Utilities of Jetson (Nano) boards for my projects

## Pins
* [Switch to alternative function (e.g. PWM, SPI, etc) of the pin:](https://docs.nvidia.com/jetson/archives/r34.1/DeveloperGuide/text/HR/ConfiguringTheJetsonExpansionHeaders.html) `sudo /opt/nvidia/jetson-io/jetson-io.py`
* [Jetson GPIO](https://github.com/NVIDIA/jetson-gpio) examples.

## UART
* Sample UART on Jetson: [Repo by JetsonHacks](https://github.com/JetsonHacksNano/UARTDemo)
* Tested with PC: use a **Serial Port Monitor** program and a **USB to TTL Serial Converter** device (TTL not RS-232).
* Tested with Arduino: use [Serial.begin($baud_rate)](https://www.arduino.cc/reference/en/language/functions/communication/serial/begin/) and [Serial.write($content)](https://www.arduino.cc/reference/en/language/functions/communication/serial/write/)
* For PWM, the ```ChangeDutyCycle()``` use percentage, so its value ranges from 0 to 100.

## ROS (ROS 1)
* Jetson (Robot) & Laptop/GroundStation connect to same network, have proper ROS Network Config in [link](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/).
* Pin enable (as shown above) is required for PWM, SPI, UART, I2C.

Use ```ros_keyboard``` package to control PWM pins of the Jetson board:
* On Laptop/Ground station, install ```ros_keyboard``` package.
* On Jetson, [Terminal 1] (by default, at ```\home``` directory) run ```python3 simple_pwm.py``` (which constantly reads case command from a text file), [Terminal 2] run ```roscore```, [Terminal 3] run ```rosrun motor_control command_read_1.py``` (which constantly writes case command to the text file, default at ```\home```). Auto run all of them by using **Startup Applications Preferences** on Ubuntu.
* Use ```rosrun keyboard keyboard``` on Laptop with WASD keys to send command.

Use **IMU MPU 9265** to make the robot run straight:
* For python, run ```python3 mpu9265_export_to_file.py``` to read IMU and store in a text file, ```python3 pwm_read_imu.py``` to read IMU data from text file and adjust the motors accordingly. For ros, ```roscore``` -> ```rosrun mpu9265_ros imu_pub_1.py``` (to publish IMU data to ros network).

Use **hall sensors** of GA25 motors:
* For python, run both ```python3 hall_1_reading.py``` and ```python3 hall_2_reading.py```, both writes each hall sensor to a text file. For ros, ```roscore``` -> ```rosrun hall_data_pub dead_reckoning_imu_mixed.py``` or ```rosrun hall_data_pub dead_reckoning_pos.py```. 

Command robot to go to a point:
* On Jetson, run all above except ```python3 pwm_read_imu.py```. Also, run ```rosrun mobile_robot_point_cmd mobile_robot_cmd_1.py```. 
* On Laptop/GroundStation, command ros message to ```pose_goal``` topic to define desired x, y position.

## MISC
* To run a script/command on boot -> Use  ```rc.local```, [link](https://www.lukmanlab.com/how-to-activing-rc-local-on-ubuntu-server-18-04/).
