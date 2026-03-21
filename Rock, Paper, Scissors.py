import time
import random
Wins = 0
Loses = 0
Draws = 0
print("type q or quit to quit.\ntype Results to see how many wins you have.")
while True:
    rock = 1
    paper = 2
    scissors = 3
    Computer = random.randint(1,3)
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
        if Computer == rock:
            print("draw.")
            Draws += 1
        elif Computer == paper:
            print("You lose.")
            Loses += 1
        else:
            print("You win!")
            Wins += 1
    elif User_input.lower() == "paper":
        if Computer == rock:
            print("You win!")
            Wins += 1
        if Computer == paper:
            print("draw.")
            Draws += 1
        else:
            print("You lose.")
            Loses += 1
    else:
        if Computer == rock:
            print("You lose!")
            Loses += 1
        elif Computer == paper:
            print("You win!")
            Wins += 1
        else:
            print("draw.")
            Draws += 1