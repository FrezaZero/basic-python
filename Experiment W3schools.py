import random

    # random chance
    
    # guaranted chance 1/10
    # 
    # guaranted chance 1/90




def general(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("try again too low")
        elif guess > random_number:
            print ("try again too high")

    print(f"yay correct, the number is {random_number}")
""""    
def computer_guess(x):
    low = 1
    high = x
    feedback :
        while feedback != "c":
            guess = random. randint(low, high)
            feedback = input(f"is ")
"""

x = 100
    