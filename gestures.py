from microbit import *

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "face up":
        display.show(Image.HEART)
    elif gesture == "face down":
        display.show(Image.GIRAFFE)
    elif gesture == "right":
        display.show(Image.ARROW_NE)
    elif gesture == "left":
        display.show(Image.ARROW_SE)
    elif gesture == "shake":
        display.show(Image.ANGRY)
    elif gesture == "freefall":
        display.show(Image.CONFUSED)
    else:
        display.clear()
