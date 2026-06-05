import random

user_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: \n").lower()
    if user_input == "q":
        break
    if user_input not in choices:
        continue

    random_number = random.randint(0, 2)
    computer_pick = choices[random_number]

    if user_input == "rock" and computer_pick == "scissors":
        print("You win! computer picked", computer_pick + ".")
        user_wins +=1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win! computer picked", computer_pick + ".")
        user_wins +=1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win! computer picked", computer_pick + ".")
        user_wins +=1

    elif user_input and computer_pick == "rock" or "paper" or "scissors":
        
        print("It's a TIE! Computer picked", computer_pick)


print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("GOODBYE!")
