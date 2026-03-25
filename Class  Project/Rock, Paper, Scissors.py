import time
import random

from fsspec.asyn import reset_lock

Wins = 0
Loses = 0
Draws = 0
print("type q or quit to quit.\ntype Results to see how many wins you have.")
while True:
    Computer = random.randint(1, 3)
    #rock = 1, paper = 2, scissors = 3
    User_input = input("type rock, paper, or scissors: ")
    if User_input.lower() == "results" or User_input.lower() == "result" or User_input.lower() == "r":
        print("Here are your results: ")
        print("----------------------------")
        print("Wins = " + str(Wins))
        print("Loses = " + str(Loses))
        print("Draws = " + str(Draws))
        print("----------------------------")
    elif User_input.lower() == "q" or User_input.lower() == "quit":
        print("loading.")
        time.sleep(1)
        print("loading..")
        time.sleep(1)
        print("loading...")
        time.sleep(1)
        print("Bye bye!")
        time.sleep(1)
        break
    elif User_input.lower() == "rock":
        if Computer == 1:
            print("-------------------------------")
            print("Computer choose rock")
            print("draw.")
            print("--------------------")
            Draws += 1
        elif Computer == 2:
            print("----------------------------")
            print("Computer choose paper")
            print("You lose.")
            print("---------------------------")
            Loses += 1
        else:
            print("-------------------------------------")
            print("Computer choose scissors")
            print("You win!")
            Wins += 1
    elif User_input.lower() == "paper":
        if Computer == 1:
            print("--------------------")
            print("Computer choose rock")
            print("You win!")
            print("---------------------")
            Wins += 1
        elif Computer == 2:
            print("--------------------")
            print("Computer choose paper")
            print("draw.")
            print("--------------------")
            Draws += 1
        else:
            print("--------------------")
            print("Computer choose scissors")
            print("You lose.")
            print("---------------------")
            Loses += 1
    else:
        if Computer == 1:
            print("--------------------")
            print("Computer choose rock")
            print("You lose!")
            print("---------------------")
            Loses += 1
        elif Computer == 2:
            print("--------------------")
            print("Computer choose paper")
            print("You win!")
            Wins += 1
        else:
            print("--------------------")
            print("Computer choose scissors")
            print("draw.")
            print("---------------------")
            Draws += 1