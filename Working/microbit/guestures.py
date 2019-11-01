from microbit import *
 
#pins
PIR_pin = pin0
LED_pin = pin1
 
while True:
    # if PIR Sensor detects motion, turn on LED
    if PIR_pin.read_digital(): 
        LED_pin.write_digital(1)
    else:
        LED_pin.write_digital(0)