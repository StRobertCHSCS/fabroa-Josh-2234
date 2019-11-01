from microbit import *

#pins
blue_light = pin2
red_light = pin1


while True:
# if PIR Sensor detects motion, turn on LED
gesture = accelerometer.current_gesture()
    if gesture == "face up":
        blue_light.write_digital(1)
    else:
        red_light.write_digital(0)
       
    
       