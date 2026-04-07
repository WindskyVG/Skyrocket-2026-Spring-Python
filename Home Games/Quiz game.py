import time
print("Welcome to the Quiz Game!\nYou can type quit to quit\nYou can also type 'results' to show the results\n(Made by me, the amazing Sophia!!!)")
print("Here are the rules:\nThere can be multiple correct choices\nChoose from A, B, C, D, or E!(Or sometimes, F!)\nHave fun!")
User_name = input("What is your name? \nPlease enter your name: ")
print("Welcome " + User_name + "!")
player_correct_answers = 0
player_incorrect_answers = 0
time.sleep(1)
while True:
    User_chose_theme = input("Choose a theme from the following list: \n-----------------\nFoxes\nMinecraft\nMinecraft Foxes\n-----------------\nChoose a theme from the list: ")
    if User_chose_theme.lower() == "foxes" or User_chose_theme.lower() == "fox":
        q1 = input("First question:\nWhat are the tails of a fox for?\nA. To keep balance\nB. To keep warm\nC. Only the one above is correct\nD. To Communicate\nE. To attract mates\n---------------\nEnter the your choice: ")
        if q1.lower() == "a":
            print("One of the correct choices!")
            player_correct_answers += 1
        elif q1.lower() == "b":
            print("One of the correct choices!")
            player_correct_answers += 1
        elif q1.lower() == "c":
            print("Wrong!")
            player_incorrect_answers += 1
        elif q1.lower() == "d":
            print("One of the correct choices!")
        elif q1.lower() == "e":
            print("Wrong!")
            player_incorrect_answers += 1
        elif q1.lower() == "f":
            print("Wrong!")
            time.sleep(1)
            print("But since it wasn't in the choices, I won't count that!")
        q2 = input("Next question!\nWhat is the maximum speed that a fox can run up to?\nA. 1 mile per hour\nB. 16 miles per hour\nC. 48 miles per hour\nD. 30 miles per hour\nE. None of the above\n---------------\nEnter the your choice: ")
        if q2.lower() == "a":
            print("Wrong!")
            player_incorrect_answers += 1
        elif q2.lower() == "b":
            print("Wrong!")
            player_incorrect_answers += 1
        elif q2.lower() == "c":
            print("Wrong!")
            player_incorrect_answers += 1
        elif q2.lower() == "d":
            print("the correct choice!")
            player_correct_answers += 1
        elif q2.lower() == "e":
            print("Wrong!")
            player_incorrect_answers += 1
        elif q2.lower() == "f":
            print("Wrong!")
            time.sleep(1)
            print("But since it wasn't in the choices, I won't count that!")
        print("That's it for today! Here are your results: \n--------------------\nYou got " + player_correct_answers + " correct!\nYou got" + player_incorrect_answers + " incorrect!\n----------------------\nLet's play again!")
        time.sleep(1)
    elif User_chose_theme.lower() == "minecraft" or User_chose_theme.lower() == "minecraft fox" or User_chose_theme.lower() == "minecraft foxes":
        print("Sorry that is not ready yet...\nChoose another theme!")