import time
#This project is about fox care
#pet fox stats: health, happiness, hunger, age, and attack
#player stats: money, sleep

# ==================================================
# Main Game Loop
# ==================================================

player_name = input("-----------------------\n'Hi! Welcome to the fox adoption center!' said ???\n'My name is Vulpix, the caretaker of these foxes.' said Vulpix\n'What is your name?' Vulpix asks\nPlease enter your name: ")
print("'Welcome " + player_name + "!'Vulpix says")
time.sleep(2)
print("'You can adopt a fox for $50!'")
time.sleep(2)
print("'What is that? You don't have enough money?'")
time.sleep(1)
print("'Well, since it's your first time here you can adopt a fox for free!'")
time.sleep(1)
print("'And we will pay you to take care of this baby fox!'exclaimed Vulpix")
time.sleep(2)
print("You got a baby fox!")
time.sleep(2)
fox_name = input("'What are you going to name your fox?'asked Vulpix\nPlease enter your fox's name: ")
print("'" + fox_name + " is a great name!'said Vulpix")
time.sleep(2)
print("'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'yowled ???")
time.sleep(1)
print("'Oh my, it seems Jasper has awoken!'said Vulpix")
time.sleep(1)
print("'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'yowled Jasper")
time.sleep(1)
print("'Well, I'd better go! Bye!'said Vulpix")
time.sleep(2)
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

    def workday():
        print("You have to go to work today, and didn't have a whole day to take care of you fox.")
        time.sleep(1.5)
    if day_num == 1:
        print("You just woke up and saw " + fox_name + "staring at you.\nYou just remembered that you got a pet fox!")
        time.sleep(1)
        workday()
        actions = input("""What will you do first?
        1. Feed """ + str(fox_name) + """
        2. Walk""")
    elif day_num % 6 == 0:
        print("")
    elif day_num%7 == 0:
        print("")