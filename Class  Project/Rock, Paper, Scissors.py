import time
import random

#add 3 more new stuff
items = []
Wins = 0
Loses = 0
Draws = 0
Coins = 0
print("type q or quit to quit.\ntype outcomes (or o) to see how many wins you have.\n(You can also type s for scissors, r for rock. or p for paper. \nYou can also type Tool Shop (or TS) to see the shop.")
while True:
    Computer = random.randint(1, 3)
    #rock = 1, paper = 2, scissors = 3
    User_input = input("type rock, paper, or scissors: ")
    if User_input.lower() == "outcomes" or User_input.lower() == "outcome" or User_input.lower() == "o":
        print("Here are your results: ")
        print("----------------------------")
        print("Wins = " + str(Wins))
        print("Loses = " + str(Loses))
        print("Draws = " + str(Draws))
        print("----------------------------")
    elif User_input.lower() == "tools shop" or User_input.lower() == "ts":
        Gun_num = 1
        print("Your coins: " + str(Coins))
        print("---------------------------")
        print("Item: Gun\nCost: 1000")
        print("---------------------")
        User_shop_input = input("type the name of the item to buy: ")
        if User_shop_input.lower() == "gun":
            while True:
                User_check = input("are you sure? Type y for yes and no for no: ")
                if User_check.lower() == "y":
                    print("ok.")
                    items = ['Gun']
                    break
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