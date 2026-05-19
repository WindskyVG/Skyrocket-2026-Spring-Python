import time
#This project is about fox care
#pet fox stats: health, happiness, hunger, age, and attack
#player stats: money, sleep

# ==================================================
# Main Game Loop
# ==================================================

fox_name = input("'What are you going to name your fox?'asked Vulpix\nPlease enter your fox's name: ")

age_max = 361
age = 1
happy_bar = 100
hunger_bar = 100
attack = 10
player_money = 1000
player_sleep_bar = 100

def stats():
    print("""==================================
          Your Fox's Stats:
          
          Age: """ + str(age) + """
          Hunger: """ + str(hunger_bar) + """
          Happiness: """ + str(happy_bar) + """
          Attack: """ + str(attack) + """
          ==================================
          ==================================
          Your Stat's:
          
          Name: """ + str(player_name) + """
          Money: """ + str(player_money) + """
          Your sleep time: """ + str(player_sleep_bar) + """%
          ==================================
          time: 7:00 am""")

for day_num in range(age_max):
    print("\n======================================")
    print(" DAY", day_num)
    print("======================================")

    if day_num == 360:
        print("Your pet fox have died.")
        time.sleep(2)
        print("But she had a great time, and died happily ever after.")
        time.sleep(2)
        print("You prepared a funeral, and your friends and family attended too, and also Vulpix.")
        time.sleep(2)
        print("Nobody said a word, but as you looked up, you saw a shape dancing in the sky, and you knew it was " + fox_name + ".")
        time.sleep(2)
        print("You got the peaceful ending!")

    def workday():
        print("You have to go to work today, and didn't have a whole day to take care of you fox.")
        time.sleep(1.5)
    if day_num == 1:
        print("You just woke up and saw " + fox_name + "staring at you.\nYou just remembered that you got a pet fox!")
        time.sleep(1)
        workday()
        #actions = input("""What will you do first?
        #1. Feed """ + str(fox_name) + """
        #2. Walk""")
    elif day_num % 6 == 0:
        print("")
    elif day_num%7 == 0:
        print("")
    elif day_num == 360:
        print("yay")