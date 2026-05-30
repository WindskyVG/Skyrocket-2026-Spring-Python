import time
endings = []
import random
#This project is about fox care
#pet fox stats: health, happiness, hunger, age, and attack
#player stats: money, sleep

# ==================================================
# Main Game Loop
# ==================================================
start_game = input("Hi! Welcome to Care For A Fox, enter start to start game.")
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
Health_bar = 100
def random_event():

    chance = random.randint(1, 100)

    if chance <= 30:

        events = [
        "Your fox got hurt by a bader!",
        "Your fox got sick",
        "You found money",
        "lost wallet",
        "Your fox got hurt by a dog",
        "You forgot to buy food for your fox!",
        "No event happened"
        ]

        event = random.choice(events)

        print("\nRandom Event:")

        if event == "Your fox got hurt by a badger":
            badger_damage = random.randint(1, 100)

def stats():
    print("""==================================
          Your Fox's Stats:
          
          Age: """ + str(age) + """
          Hunger: """ + str(hunger_bar) + """
          Happiness: """ + str(happy_bar) + """
          Health: """ + str(Health_bar) + """
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


    def workday():
        print("You have to go to work today, and didn't have a whole day to take care of you fox.")
        time.sleep(1.5)
    if day_num == 1:

        print("You just woke up and saw " + fox_name + "staring at you.\nYou just remembered that you got a pet fox!")
        time.sleep(1)
        workday()
        stats()
        actions = input("""What will you do first? (You only have time to do 2, and 1 more after work)
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
        if actions != 2 and actions2 != 2:
            Health_bar -= 5
        player_money_from_work = random.randint(50, 120)
        print("You got home from work and earned $" + str(player_money_from_work))
        player_money += player_money_from_work
        time.sleep(1.5)
        player_money_for_food = random.randint(30, 50)
        print("But you also ate today and spent $" + str(player_money_for_food))
        player_money -= player_money_for_food
        actions3 = input("""What will you do third?
                                1. Feed """ + str(fox_name) + """
                                2. Walk """ + str(fox_name) + """
                                3. Play with """ + str(fox_name) + """
                                4. Do nothing""")
        if actions2 == "1" and actions == "1" and actions3 == "1":
            hunger_bar += 30
        elif actions3 == "2":
            happy_bar += 30
        elif actions3 == "3" and actions == "3" and actions3 == "3":
            happy_bar += 20
        elif actions3 == "4":
            happy_bar -= 10
        if actions != 2 and actions2 != 2:
            Health_bar -= 5
        print("You went to the store")

    elif day_num % 6 == 0:
        print("Today is a Saturday! you get to do 6 actions!")
        actions = input("""What will you do first?
                1. Feed """ + str(fox_name) + """
                2. Walk """ + str(fox_name) + """
                3. Play with """ + str(fox_name) + """
                4. Do nothing
                5. Watch movies with """ + str(fox_name) + """
                6. Brush """ + str(fox_name) + """
                7. Wash """ + str(fox_name))
        if actions == "1":
            hunger_bar = 100
        elif actions == "2":
            happy_bar += 10
        elif actions == "3":
            happy_bar = 100
        elif actions == "4":
            happy_bar -= 10
        elif actions == "5":
            happy_bar = 100
        elif actions == "6":
            happy_bar += 15
        elif actions == "7":
            Health_bar += 3
            happy_bar -= 5
        actions2 = input("""What will you do second?
                1. Feed """ + str(fox_name) + """
                2. Walk """ + str(fox_name) + """
                3. Play with """ + str(fox_name) + """
                4. Do nothing
                5. Watch a movie with """ + str(fox_name) + """
                6. Brush """ + str(fox_name) + """
                7. Wash """ + str(fox_name))
        if actions2 == "1" and actions == "1":
            hunger_bar += 30
        elif actions2 == "2":
            happy_bar += 30
        elif actions2 == "3" and actions == "3":
            happy_bar += 20
        elif actions2 == "4":
            happy_bar -= 10
        elif actions2 == "5":
            happy_bar = 100
        elif actions2 == "6":
            happy_bar += 15
        elif actions2 == "7":
            Health_bar += 3
            happy_bar -= 5
        actions3 = input("""What will you do third?
                        1. Feed """ + str(fox_name) + """
                        2. Walk """ + str(fox_name) + """
                        3. Play with """ + str(fox_name) + """
                        4. Do nothing
                        5. Watch a movie with """ + str(fox_name) + """
                        6. Brush """ + str(fox_name) + """
                        7. Wash """ + str(fox_name))
        if actions2 == "1" and actions == "1" and actions3 == "1":
            hunger_bar += 30
        elif actions3 == "2":
            happy_bar += 30
        elif actions3 == "3" and actions == "3":
            happy_bar += 20
        elif actions3 == "4":
            happy_bar -= 10
        elif actions3 == "5":
            happy_bar = 100
        elif actions3 == "6":
            happy_bar += 15
        elif actions3 == "7":
            Health_bar += 3
            happy_bar -= 5
        actions4 = input("""What will you do fourth?
                                1. Feed """ + str(fox_name) + """
                                2. Walk """ + str(fox_name) + """
                                3. Play with """ + str(fox_name) + """
                                4. Do nothing
                                5. Watch a movie with """ + str(fox_name) + """
                                6. Brush """ + str(fox_name) + """
                                7. Wash """ + str(fox_name))
        if actions2 == "1" and actions == "1" and actions3 == "1" and actions4 == "1":
            hunger_bar += 30
        elif actions4 == "2":
            happy_bar += 30
        elif actions4 == "3" and actions == "3":
            happy_bar += 20
        elif actions4 == "4":
            happy_bar -= 10
        elif actions4 == "5":
            happy_bar = 100
        elif actions4 == "6":
            happy_bar += 15
        elif actions4 == "7":
            Health_bar += 3
            happy_bar -= 5
        actions5 = input("""What will you do fifth?
                                1. Feed """ + str(fox_name) + """
                                2. Walk """ + str(fox_name) + """
                                3. Play with """ + str(fox_name) + """
                                4. Do nothing
                                5. Watch a movie with """ + str(fox_name) + """
                                6. Brush """ + str(fox_name) + """
                                7. Wash """ + str(fox_name))
        if actions2 == "1" and actions == "1" and actions3 == "1" and actions4 == "1" and actions5 == "1":
            hunger_bar += 30
        elif actions5 == "2":
            happy_bar += 30
        elif actions5 == "3" and actions == "3":
            happy_bar += 20
        elif actions5 == "4":
            happy_bar -= 10
        elif actions5 == "5":
            happy_bar = 100
        elif actions5 == "6":
            happy_bar += 15
        elif actions5 == "7":
            Health_bar += 3
            happy_bar -= 5
        actions6 = input("""What will you do sixth?
                                1. Feed """ + str(fox_name) + """
                                2. Walk """ + str(fox_name) + """
                                3. Play with """ + str(fox_name) + """
                                4. Do nothing
                                5. Watch a movie with """ + str(fox_name) + """
                                6. Brush """ + str(fox_name) + """
                                7. Wash """ + str(fox_name))
        if actions2 == "1" and actions == "1" and actions3 == "1" and actions4 == "1" and actions5 == "1" and actions6 == "1":
            hunger_bar += 30
        elif actions6 == "2":
            happy_bar += 30
        elif actions6 == "3" and actions == "3":
            happy_bar += 20
        elif actions6 == "4":
            happy_bar -= 10
        elif actions6 == "5":
            happy_bar = 100
        elif actions6 == "6":
            happy_bar += 15
        elif actions6 == "7":
            Health_bar += 3
            happy_bar -= 5
        if actions != 2 and actions2 != 2 and actions3 != 2 and actions4 != 2 and actions5 != 2 and actions6 != 2:
            Health_bar -= 8
        if Health_bar > 100:
            Health_bar = 100
        hunger_bar -= 40
        player_money_for_food = random.randint(50, 70)
        print("But you also ate today and spent $" + str(player_money_for_food))
        player_money -= player_money_for_food
    elif day_num%7 == 0:
        print("Today is a Sunday! You get 6 actions!")
        actions = input("""What will you do first?
                        1. Feed """ + str(fox_name) + """
                        2. Walk """ + str(fox_name) + """
                        3. Play with """ + str(fox_name) + """
                        4. Do nothing
                        5. Watch movies with """ + str(fox_name) + """
                        6. Brush """ + str(fox_name) + """
                        7. Wash """ + str(fox_name))
        if actions == "1":
            hunger_bar = 100
        elif actions == "2":
            happy_bar += 10
        elif actions == "3":
            happy_bar = 100
        elif actions == "4":
            happy_bar -= 10
        elif actions == "5":
            happy_bar = 100
        elif actions == "6":
            happy_bar += 15
        elif actions == "7":
            Health_bar += 3
            happy_bar -= 5
        actions2 = input("""What will you do second?
                        1. Feed """ + str(fox_name) + """
                        2. Walk """ + str(fox_name) + """
                        3. Play with """ + str(fox_name) + """
                        4. Do nothing
                        5. Watch a movie with """ + str(fox_name) + """
                        6. Brush """ + str(fox_name) + """
                        7. Wash """ + str(fox_name))
        if actions2 == "1" and actions == "1":
            hunger_bar += 30
        elif actions2 == "2":
            happy_bar += 30
        elif actions2 == "3" and actions == "3":
            happy_bar += 20
        elif actions2 == "4":
            happy_bar -= 10
        elif actions2 == "5":
            happy_bar = 100
        elif actions2 == "6":
            happy_bar += 15
        elif actions2 == "7":
            Health_bar += 3
            happy_bar -= 5
        actions3 = input("""What will you do third?
                                1. Feed """ + str(fox_name) + """
                                2. Walk """ + str(fox_name) + """
                                3. Play with """ + str(fox_name) + """
                                4. Do nothing
                                5. Watch a movie with """ + str(fox_name) + """
                                6. Brush """ + str(fox_name) + """
                                7. Wash """ + str(fox_name))
        if actions2 == "1" and actions == "1" and actions3 == "1":
            hunger_bar += 30
        elif actions3 == "2":
            happy_bar += 30
        elif actions2 == "3" and actions == "3" and actions3 == "3":
            happy_bar += 20
        elif actions3 == "4":
            happy_bar -= 10
        elif actions3 == "5":
            happy_bar = 100
        elif actions3 == "6":
            happy_bar += 15
        elif actions3 == "7":
            Health_bar += 3
            happy_bar -= 5
        actions4 = input("""What will you do fourth?
                                        1. Feed """ + str(fox_name) + """
                                        2. Walk """ + str(fox_name) + """
                                        3. Play with """ + str(fox_name) + """
                                        4. Do nothing
                                        5. Watch a movie with """ + str(fox_name) + """
                                        6. Brush """ + str(fox_name) + """
                                        7. Wash """ + str(fox_name))
        if actions2 == "1" and actions == "1" and actions3 == "1" and actions4 == "1":
            hunger_bar += 30
        elif actions4 == "2":
            happy_bar += 30
        elif actions2 == "3" and actions == "3" and actions3 == "3" and actions4 == "3":
            happy_bar += 20
        elif actions4 == "4":
            happy_bar -= 10
        elif actions4 == "5":
            happy_bar = 100
        elif actions4 == "6":
            happy_bar += 15
        elif actions4 == "7":
            Health_bar += 3
            happy_bar -= 5
        actions5 = input("""What will you do fifth?
                                        1. Feed """ + str(fox_name) + """
                                        2. Walk """ + str(fox_name) + """
                                        3. Play with """ + str(fox_name) + """
                                        4. Do nothing
                                        5. Watch a movie with """ + str(fox_name) + """
                                        6. Brush """ + str(fox_name) + """
                                        7. Wash """ + str(fox_name))
        if actions2 == "1" and actions == "1" and actions3 == "1" and actions4 == "1" and actions5 == "1":
            hunger_bar += 30
        elif actions5 == "2":
            happy_bar += 30
        elif actions2 == "3" and actions == "3" and actions3 == "3" and actions4 == "3" and actions5 == "3":
            happy_bar += 20
        elif actions5 == "4":
            happy_bar -= 10
        elif actions5 == "5":
            happy_bar = 100
        elif actions5 == "6":
            happy_bar += 15
        elif actions5 == "7":
            Health_bar += 3
            happy_bar -= 5
        actions6 = input("""What will you do sixth?
                                        1. Feed """ + str(fox_name) + """
                                        2. Walk """ + str(fox_name) + """
                                        3. Play with """ + str(fox_name) + """
                                        4. Do nothing
                                        5. Watch a movie with """ + str(fox_name) + """
                                        6. Brush """ + str(fox_name) + """
                                        7. Wash """ + str(fox_name))
        if actions2 == "1" and actions == "1" and actions3 == "1" and actions4 == "1" and actions5 == "1" and actions6 == "1":
            hunger_bar += 30
        elif actions6 == "2":
            happy_bar += 30
        elif actions2 == "3" and actions == "3" and actions3 == "3" and actions4 == "3" and actions5 == "3" and actions6 == "3":
            happy_bar += 20
        elif actions6 == "4":
            happy_bar -= 10
        elif actions6 == "5":
            happy_bar = 100
        elif actions6 == "6":
            happy_bar += 15
        elif actions6 == "7":
            Health_bar += 3
            happy_bar -= 5
        if actions != 2 and actions2 != 2 and actions3 != 2 and actions4 != 2 and actions5 != 2 and actions6 != 2:
            Health_bar -= 8
        if Health_bar > 100:
            Health_bar = 100
        hunger_bar -= 30
        player_money_for_food = random.randint(50, 70)
        print("But you also ate today and spent $" + str(player_money_for_food))
        player_money -= player_money_for_food
    else:
        workday()
        stats()
        time.sleep(2)
        actions = input("""What will you do first? (You only have time to do 2, and after work 1 more)
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
        player_money_from_work = random.randint(50, 120)
        print("You got home from work and earned $" + str(player_money_from_work))
        player_money += player_money_from_work
        time.sleep(1.5)
        player_money_for_food = random.randint(20, 50)
        print("But you also ate today and spent $" + str(player_money_for_food))
        player_money -= player_money_for_food
        actions3 = input("""What will you do third?
                        1. Feed """ + str(fox_name) + """
                        2. Walk """ + str(fox_name) + """
                        3. Play with """ + str(fox_name) + """
                        4. Do nothing""")
        if actions3 == "1" and actions == "1" and actions3 == "1":
            hunger_bar += 30
        elif actions3 == "2":
            happy_bar += 30
        elif actions3 == "3" and actions == "3" and actions3 == "3":
            happy_bar += 20
        elif actions3 == "4":
            happy_bar -= 10
        if actions != 2 and actions2 != 2 and actions3 != 2:
            Health_bar -= 5

    if day_num == 360:
        print("Your pet fox have died.")
        time.sleep(2)
        print("But it had a great time, and died happily ever after.")
        time.sleep(2)
        print("You prepared a funeral, and your friends and family attended too, and also Vulpix.")
        time.sleep(2)
        print("Nobody said a word, but as you looked up, you saw a shape dancing in the sky, and you knew it was " + fox_name + ".")
        time.sleep(2)
        print("You got the Peaceful Ending!")
        endings.append("Peaceful Ending")
if hunger_bar > hunger_bar_max:
    print("Your fox died from eating too much.")
    time.sleep(2)
    print("You got the Fat Ending!")
    endings.append("Fat Ending")
if happy_bar > happy_bar_max:
    print("Your fox died from being too happy.")
    time.sleep(2)
    print("You got the Happy Ending?!")
    endings.append("Happy Ending?")