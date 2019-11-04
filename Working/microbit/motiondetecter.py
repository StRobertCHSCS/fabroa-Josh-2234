from microbit import*


# pins
Motion_detector = pin0
Blue_light = pin1
Red_light = pin2

while True:
    # if motion sensor detects motion, turn a light, turn on both light.
    if button_a.is_pressed():
        Blue_light.write_digital(1)
        Red_light.write_digital(0)

    if Motion_detector.read_digital() > 0 and Blue_light.read_digital() == 1:
        Red_light.write_digital(1)

    elif button_b.is_pressed():
        Blue_light.write_digital(0)
        Red_light.write_digital(1)

    else:
        Blue_light.write_digital(0) 
        Red_light.write_digital(0)
