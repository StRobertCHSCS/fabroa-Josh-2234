from microbit import*


# pins
Motion_detector = pin0
Blue_light = pin1
Red_light = pin2

while True:
    # if motion sensor detects motion, turn a light, or make a sound
    if Motion_detector.read_digital() and button_a.is_pressed():
        Blue_light.write_digital(0)
        Red_light.write_digital(0)

    elif Motion_detector.read_digital() and button_b.is_pressed() and button_a._pressed():
        Blue_light.write_digital(1)
        Red_light.write_digital(1)

    
    elif Motion_detector.read_digital() and button_b.is_pressed():
        Blue_light.write_digital(0)
        Red_light.write_digital(1)

    else:
        Blue_light.write_digital(0)
        Red_light.write_digital(0)
       
