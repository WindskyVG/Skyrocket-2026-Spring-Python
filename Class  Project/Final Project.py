import time
endings = []
import random
#This project is about fox care
#pet fox stats: health, happiness, hunger, age, and attack
#player stats: money, sleep

# ==================================================
# Main Game Loop
# ==================================================
print("""'Hi! Welcome to the adoption center for foxes. I'm Vulpix, the caretaker!'said Vulpix
You saw a sign that said '$50 for 1 fox'
'I don't have enough money.' You say.
'It's okay! I'll give you one to care for free, and we can pay you.'Said Vulpix
You got 1000 dollars
'These are the starter money to care for your pet. Also, why don't you get a job?'continued Vulpix
'Also, don't feed it or play with it too much!'
You decide to take her advice about the work.""")
time.sleep(1)
fox_gender = random.randint(1, 2)
if fox_gender == 1:
    fox_gender = "girl"
elif fox_gender == 2:
    fox_gender = "boy"
print("You got a fox! it is a " + fox_gender + ".")
time.sleep(2)
fox_name = input("'What are you going to name your fox?'asked Vulpix\nPlease enter your fox's name: ")
age_max = 361
age = 1
happy_bar = 75
hunger_bar = 50
attack = 10
player_money = 1000
player_sleep_bar = 100
hunger_bar_max = 200
happy_bar_max = 200
def stats():
    print("""==================================
          Your Fox's Stats:
          
          Age: """ + str(age) + """
          Hunger: """ + str(hunger_bar) + """
          Happiness: """ + str(happy_bar) + """
          Attack: """ + str(attack) + """
          gender: """ + str(fox_gender) + """
          ==================================
          ==================================
          Your Stat's:
          
          Money: """ + str(player_money) + """
          Your sleep bar (100 = full): """ + str(player_sleep_bar) + """%
          ==================================
          time: 7:00 am""")

for day_num in range(age_max):
    print("\n======================================")
    print(" DAY", day_num)
    print("======================================")

    if day_num == 360:
        print("Your pet fox have died.")
        time.sleep(2)
        print("But it had a great time, and died happily ever after.")
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
        stats()
        actions = input("""What will you do first? (You only have time to do 2)
        1. Feed """ + str(fox_name) + """
        2. Walk """ + str(fox_name) + """
        3. Play with """ + str(fox_name) + """
        4. Do nothing""")
        if actions == "1":
            hunger_bar = 100
        elif actions == "2":
            happy_bar += 10
        elif actions == "3":
            happy_bar = 100
        elif actions == "4":
            happy_bar -= 10
        actions2 = input("""What will you do second?
        1. Feed """ + str(fox_name) + """
        2. Walk """ + str(fox_name) + """
        3. Play with """ + str(fox_name) + """
        4. Do nothing""")
        if actions2 == "1" and actions == "1":
            hunger_bar += 30
        elif actions2 == "2":
            happy_bar += 30
        elif actions2 == "3" and actions == "3":
            happy_bar += 20
        elif actions2 == "4":
            happy_bar -= 10

    elif day_num % 6 == 0:
        print("")
    elif day_num%7 == 0:
        print("")
    else:
        workday()
        stats()
        time.sleep(2)
        actions = input("""What will you do first? (You only have time to do 2)
                1. Feed """ + str(fox_name) + """
                2. Walk """ + str(fox_name) + """
                3. Play with """ + str(fox_name) + """
                4. Do nothing""")
        if actions == "1":
            hunger_bar = 100
        elif actions == "2":
            happy_bar += 10
        elif actions == "3":
            happy_bar = 100
        elif actions == "4":
            happy_bar -= 10
        actions2 = input("""What will you do second?
                1. Feed """ + str(fox_name) + """
                2. Walk """ + str(fox_name) + """
                3. Play with """ + str(fox_name) + """
                4. Do nothing""")
        if actions2 == "1" and actions == "1":
            hunger_bar += 30
        elif actions2 == "2":
            happy_bar += 30
        elif actions2 == "3" and actions == "3":
            happy_bar += 20
        elif actions2 == "4":
            happy_bar -= 10