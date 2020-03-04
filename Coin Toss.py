c = ['heads', 'tails']
print("")
input("Coin Toss, A project by Lucas.")
print("")
from random import shuffle
pscore = 0
s = 1
while s == 1:
  shuffle(c)
  comp = c[0]
  print("")
  player = input("Heads or Tails?\n")
  if player.strip(" ").lower() == "heads" and comp == "heads":
    print("It was Heads! You win!")
    pscore += 1
  elif player.strip(" ").lower() == "heads" and comp == "tails":
    print("It was Tails. Better luck next time!")
  elif player.strip(" ").lower() == "tails" and comp == "tails":
    print("It was Tails! You win!")
    pscore += 1
  elif player.strip(" ").lower() == "tails" and comp == "heads":
    print("It was Heads. Better luck next time.")
  else:
    print("Ummm... that's not a valid answer...")
  print("")
  answer = input("Would you like to keep playing?\n")
  if answer.strip(" ").lower() == "no":
    s += 1
  elif answer.strip(" ").lower() == "yes":
    input("Okay! Currently you have won " + str(pscore)+" coin tosses.")
  else:
    print("You can´t say that...")
    quit()
quit()
