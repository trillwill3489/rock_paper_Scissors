import random
print("Let's play rock, paper, scissors! What do you chose?")
player = input().lower()
options = ["rock", "paper", "scissors"]
computer = random.choice(options)

while player in options:
    break
else:
    print("ERROR! You did not select an option!")
    
if player == "rock":
    if computer == "paper":
        print("The computer picks... paper! You lose :(")
    elif computer == "scissors":
        print("The computer picks... scissors! You win!!")
    else:
        print("The computer picks... rock! The game is a draw...")
        
elif player == "paper":
    if computer == "scissors":
        print("The computer picks... scissors! You lose :(")
    elif computer == "rock":
        print("The computer picks... rock! You win!!")
    else:
        print("The computer picks... paper! The game is a draw...")
        
else:
    if computer == "rock":
        print("The computer picks... rock! You lose :(")
    elif computer == "paper":
        print("The computer picks... paper! You win!!")
    else:
        print("The computer picks... scissors! The game is a draw...")