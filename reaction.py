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
# Add score of each the player
left_score = right_score = 0
# Add reaction time of each other
left_time = right_time = 0

def pressed(button):
    global winner_declared, left_score, right_score, left_time, right_time
    if button.pin.number == 14:
        if winner_declared == False:
            print("<%s won the game>" % (left_name))
            left_score += 1
        left_time = time()
        winner_declared = True
    elif button.pin.number == 15:
        if winner_declared == False:
            print("<%s won the game>" % (right_name))
            right_score += 1
        right_time = time()
        winner_declared = True

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
    # Get the time when the light is off
    off_time = time()

    sleep(2)
    
    # Output the scores of each playe
    print("--------")
    print(" Scores ")
    print("--------")
    print("<Score of %s: %d>" % (left_name, left_score))
    print("<Score of %s: %d>" % (right_name, right_score))

    # Output the reaction time
    print("---------------")
    print(" Reaction Time ")
    print("---------------")
    print("<Reaction time of %s: %.2f>" % (left_name, (left_time - off_time)))
    print("<Reaction time of %s: %.2f>" % (right_name, (right_time - off_time)))

    # Ask user if they want to continue
    print("---------")
    print(" Options ")
    print("---------")
    print("0) Exit")
    print("1) Continue")
    if get_option() == 0:
        break

# Show the program is terminated
print("<Bye>")
