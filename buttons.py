from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.MUSIC_CROTCHET)
    elif button_b.is_pressed():
        display.show(Image.MUSIC_QUAVER)
    else:
        display.clear()
