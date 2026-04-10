# AUTHOR: Leo Li
# DATE: 2026/4/9 - 2026/4/10

from gpiozero import LED, Button
from time import sleep, time
from random import uniform
import sys

# Set the pins
led = LED(4)
right_button = Button(15)
left_button = Button(14)

print("=============")
print(" Button Game ")
print("=============")

print("-------------")
print(" Names Input ")
print("-------------")

left_name = input("[Left player name is]\n")
right_name = input("[Right player name is]\n")

# Add a status variable to show only a winner
winner_declared = False

def pressed(button):
    global winner_declared
    if winner_declared:
        return
    winner_declared = True
    if button.pin.number == 14:
        print("<%s won the game>" % (left_name))
    elif button.pin.number == 15:
        print("<%s won the game>" % (right_name))

def get_option():
    option = int(input("[Enter your option]\n"))
    return option

# Set the Event
right_button.when_pressed = pressed
left_button.when_pressed = pressed

print("-------")
print(" Rules ")
print("-------")
print("""When the game begin, the light turns on.
You will press the botton of your side
as soon as you can when the light turn
off. The faster one will be the winner.""")

input("<Press [Enter] to begin>")

print("<Game starting ...>")
sleep(1)

print("------------")
print(" Game Begin ")
print("------------")

while True:
    # Reclaim the status variable
    winner_declared = False

    led.on()
    print("<Press only after the light turns off>")
    sleep(uniform(5, 10))
    print("<Pressed now!>")
    led.off()

    sleep(1)
    
    print("---------")
    print(" Options ")
    print("---------")
    print("0) Exit")
    print("1) Continue")
    if get_option() == 0:
        break

print("<Bye>")
