# Imports
import os

import random
import time
# Variables

# This function clears the screen and clears it on start up
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_terminal()
# This is the Brains of the game. The terminal clears and updates once
# every second
def main():
    x = 0
    inventory = []
    while True:
        print("option 1: collect an egg")
        print()
        print("option 2: inventory")
        user_input = input("choose an option ")
        # If the user inputs 1 than this code will play out
        if user_input == "1":
            clear_terminal()
            user_input_name = input("Make a name for your dragon egg! ")
            user_input_color = input("what does it look like? ")
            rand_size = random.randint(1,5)

            new_egg = Egg(user_input_name, user_input_color, rand_size)
            inventory.append(new_egg)
            time.sleep(3)
       
        # If the user enters 2 than this code will play out
        if user_input == "2":
            clear_terminal()
            for egg in inventory:
                print(f"{egg.name} | {egg.health}")
            input("press enter to continue")
            clear_terminal()            
            

        time.sleep(1)
        clear_terminal()
        
class Egg:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
        self. temperature = 50
        self.health = 50
        self.incubation = 0

        print(f"You collected {self.name}, it is {self.color}, and it size {self.size}")
        

main()