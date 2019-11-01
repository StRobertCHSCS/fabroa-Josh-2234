from microbit import *
import music 
  
#pins
PIR_sensor = pin0
LED_red = pin1
sound = pin2
 
while True:
    # if PIR Sensor detects motion, turn on LED
    if PIR_sensor.read_digital(): 
        LED_red.write_digital(1)
        music.play ('f3:4' , pin=sound)
    else:
        LED_red.write_digital(0)