import random

print("Choose rock (r), paper (p) or scissors (s) to play 3 times")

#Counters for losses, wins and ties initialized i zero

wins = 0
losses = 0
ties = 0

#Create a loop for 3 games

for i in range(3):
  player1 = str(input())

  if player1 == "r":
    print("Player choose ROCK")
  elif player1 == "p":
    print("Player choose PAPER")
  elif player1 == "s":
    print("Player choose SCISSORS")
  else:
    print("Try again")
    continue

#Computer makes its choice
  computer_choice = random.randint(0,3)

  if computer_choice == 0:
    print("Computer chose ROCK")
  elif computer_choice == 1:
    print("Computer chose PAPER")
  else:
    print("Computer chose SCISSORS")

#Starts comparing choices

  if player1 == "r":
    if computer_choice == 0:
      print("It's a tie")
      ties+=1
    elif computer_choice == 1:
      print("You loose")
      losses+=1
    else:
      print("You win")
      wins+=1
  elif player1 == "p":
    if computer_choice == 0:
      print("You win")
      wins+=1
    elif computer_choice == 1:
      print("It's a tie")
      ties+=1
    else:
      print("You loose")
      losses+=1
  else: #player1 == "s"
    if computer_choice == 0:
      print("You loose")
      losses+=1
    elif computer_choice == 1:
      print("You win")
      wins+=1
    else:
      print("It's a tie")
      ties+=1

#Determines the winner

print("The score: Wins " + str(wins) + ", Losses " + str(losses) + ", Ties "+str(ties))
if wins>=2:
  print("You won!!!!")
else:
  print("You loose everything!")
  