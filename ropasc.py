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
        
