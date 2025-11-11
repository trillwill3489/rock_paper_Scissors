import random
print("Let's play rock, paper, scissors! What do you chose?")
player = input().lower()
options = ["rock", "paper", "scissors"]
computer = random.choice(options)
print(computer)