from microbit import *

player_x = 2
y_value = 2
integers = [1, -1]
while True:
    if button_a.was_pressed():
        display.set_pixel(player_x, y_value, 0)
        player_x -= 1
    if button_b.was_pressed():
        display.set_pixel(player_x, y_value, 0)
        playfrom microbit import *er_x += 1
    if y_value == 0:
        y_value += 1
    else:
        if y_value == 4:
            y_value -= 1
            break
        else:
            y_value += int((random.choice(integers))
            break
    
    display.set_pixel(player_x, y_value, 9)
