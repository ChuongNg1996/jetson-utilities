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
* Jetson (Robot) & Laptop/GroundStation connect to same network, have proper ROS Network Config in [link](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/)
Use ```ros_keyboard``` package to control PWM pins of the Jetson board:
* On Laptop/Ground station, install ```ros_keyboard``` package.
* ON Jetson, [Terminal 1] (by default, at ```\home``` directory) run ```python3 simple_pwm.py``` (which constantly read case command from a text file), [Terminal 2] run ```roscore```, [Terminal 3] run ```rosrun motor_control command_read_1.py```. Auto run all of them by using ***Startup Applications Preferences*** on Ubuntu.
