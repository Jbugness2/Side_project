# Imports
import os
os.system('cls' if os.name == 'nt' else 'clear')
import random
import time
# Variables

# This is the Brains of the game. The terminal clears and updates once
# every second
def main():
    x = 0
    while True:
        print("option 1: collect an egg")
        print()
        print("option 2: inventory")
        user_input = input("choose an option ")

        if user_input == "1":
            user_input_name = input("Make a name for your dragon egg! ")
            user_input_color = input("what does it look like? ")

            rand_size = random.randint(1,5)

            Egg(user_input_name, user_input_color, rand_size)

        if user_input == "2":
            pass

        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        
class Egg:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
        self. temperature = 50
        self.health = 50
        self.incubation = 0

        print(f"You collected {self.name}, it is {self.color}, and it size {self.size}")
        time.sleep(5)

main()