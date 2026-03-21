import time
Wins = 0
while True:
    rock = 1
    paper = 2
    scissors = 3
    Computer = (rock, paper, scissors)
    print("type q or quit to quit.\ntype Wins to see how many wins you have.")
    User_input = input("type rock, paper, or scissors: ")
    if User_input.lower() == "wins" or User_input.lower() == "win" or User_input.lower() == "w":
        print("Here is the number of your wins: ")
        print(Wins)
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
        elif Computer == paper:
            print("You lose.")
        else:
            print("You win!")
            Wins += 1
    elif User_input.lower() == "paper":
        if Computer == rock:
            print("You win!")
            Wins += 1
        if Computer == paper:
            print("draw.")
        else:
            print("You lose.")
    else:
        if Computer == rock:
            print("You lose!")
        elif Computer == paper:
            print("You win!")
            Wins += 1
        else:
            print("draw.")
