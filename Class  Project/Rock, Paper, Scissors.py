import time
import random

#add 3 more new stuff
items = []
Wins = 0
Loses = 0
Draws = 0
Coins = 0
while True:
    Input = input("type q or quit to quit.\ntype outcomes (or o) to see how many wins you have.\n(You can also type s for scissors, r for rock. or p for paper. \nYou can also type Tool Shop (or TS) to see the shop.\nDon't type rock or paper or scissors yet and don't close this tab, you will lose all of your progress.\n Enter start to start. (Or other): ")
    if Input.lower() == "tools shop" or Input.lower() == "ts":
        Gun = 1
        print("Your coins: " + str(Coins))
        print("---------------------------")
        print("Item: Gun\nCost: 1000")
        print("---------------------")
        User_shop_input = input("type the name of the item to buy: ")
        if User_shop_input.lower() == "gun":
            User_check = input("are you sure? Type y for yes and no for no: ")
            if User_check.lower() == "y" or User_check.lower() == "yes":
                print("ok.")
                if Coins >= 0:
                    items.append(User_shop_input)
                    print("exiting tools shop")
                else:
                    print("error. Purchase unsuccessful.")
                    print("exiting tool shop")
            elif User_check.lower() == "no" or User_check.lower() == "n":
                print("ok")
                print("exiting tools shop")
    elif Input.lower() == "q" or Input.lower() == "quit":
        print("loading.")
        time.sleep(1)
        print("loading..")
        time.sleep(1)
        print("loading...")
        time.sleep(1)
        print("Bye bye!")
        time.sleep(1)
    else:
        while True:
            Computer = random.randint(1, 3)
            # rock = 1, paper = 2, scissors = 3
            User_input = input("type rock, paper, or scissors: ")
            if User_input.lower() == "outcomes" or User_input.lower() == "outcome" or User_input.lower() == "o":
                print("Here are your results: ")
                print("----------------------------")
                print("Wins = " + str(Wins))
                print("Loses = " + str(Loses))
                print("Draws = " + str(Draws))
                print("----------------------------")
            elif User_input.lower() == "rock" or User_input.lower() == "r":
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
            elif User_input.lower() == "paper" or User_input.lower() == "p":
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
            elif User_input.lower() == "scissors" or User_input.lower() == "s":
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
            else:
                print("Sorry that answer is unavailable...")