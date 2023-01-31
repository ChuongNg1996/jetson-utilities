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
