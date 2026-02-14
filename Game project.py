import time, random
Playerwins = 0
Enemywins = 0
print('By the way you and the enemy get random health and attacks..')
for i in range(1, 6):
    time.sleep(2) #add a notificeable pause between rounds
    print('\n-------- Now starting round ' + str(i) + ' -------')#round header
    Playerhealth = random.randint(100, 150)
    Enemyhealth = random.randint(100, 150)
    Playerattack = random.randint(10, 40)
    Enemyattack = random.randint(10, 40)
    Playerheal = random.randint(10, 30)
    Enemyheal = random.randint(10, 30)
    Enemychoice = random.randint(3, 4)
    # display both chracter's stats.
    print('Player (You)\n' + 'HP: ' + str(Playerhealth) + '\nAttack: ' + str(Playerattack) + '\n Heal: ' + str(Playerheal) + '\n Player rounds winned: ' + str(Playerwins))#the \n means a new line
    print('------------------------------')
    time.sleep(2)
    print('Enemy \n' + 'HP: ' + str(Enemyhealth) + '\nAttack: ' + str(Enemyattack) + '\n Heal: ' + str(Enemyheal) + '\n Enemy rounds winned: ' + str(Enemywins))
    print('------------------------------')
    time.sleep(2)
    # combat loop
    while (Playerhealth > 0) and (Enemyhealth > 0):
        Playermiss = random.randint(0, 100)
        Enemymiss = random.randint(0, 100)
        Playerhealth = Playerhealth - Enemyattack
        Enemyhealth = Enemyhealth - Playerattack
        Playerchoice = input('What are you going to do? 1 to attack, 2 to heal.')
        if Playerchoice == '1' and Enemychoice == '3':
            if Enemymiss < 70 and Playermiss >= 70:
                print('You attacked the Enemy, HP left: ' + str(Enemyhealth))
                Playerhealth = Playerhealth + Enemyattack
                print('Enemy missed you, Player (You) HP left: ' + str(Playerhealth))
                print('-----------------------------------------------')
                # Playerhealth is an interger, so we use str(...) to concatenate with strings
            elif Enemymiss >= 70 and Playermiss >= 70:
                Playerhealth = Playerhealth + Enemyattack
                Enemyhealth = Enemyhealth + Playerattack
                print('Enemy missed you, Player (You) HP left: ' + str(Playerhealth))
                print('You missed the Enemy, Enemy HP left: ' + str(Enemyhealth))
                print('-----------------------------------------------')
            elif Playermiss < 70 and Enemymiss >= 70:
                print('Enemy attacked you, Player (You) HP left: ' + str(Playerhealth))
                Enemyhealth = Enemyhealth + Playerattack
                print('You missed the Enemy, Enemy HP left: ' + str(Enemyhealth))
                print('-----------------------------------------------')
            else:
                print('Enemy attacked you, Player (You) HP left: ' + str(Playerhealth))
                print('You attacked the Enemy, Enemy HP left: ' + str(Enemyhealth))
                print('-----------------------------------------------')
            time.sleep(2.5)
        if Playerchoice == '1' and Enemychoice == '4':
            if Playermiss >= 70:
                print('You attacked the Enemy, HP left: ' + str(Enemyhealth))
                Playerhealth = Playerhealth + Enemyattack
                Enemyhealth = Enemyhealth + Enemyheal
                print('Enemy healed, enemy HP left: ' + str(Enemyhealth))
                print('-----------------------------------------------')
                # Playerhealth is an interger, so we use str(...) to concatenate with strings
            elif Playermiss < 70:
                Enemyhealth = Enemyhealth + Enemyheal
                print('Enemy healed, Enemy HP left: ' + str(Enemyhealth))
                Enemyhealth = Enemyhealth + Playerattack
                print('You missed the Enemy, Enemy HP left: ' + str(Enemyhealth))
                print('-----------------------------------------------')
            time.sleep(2.5)
        if Playerchoice == '2' and Enemychoice == '4':
            Playerhealth = Playerhealth + Playerheal
            print('You healed, Player (You) HP left: ' + str(Playerhealth))
            Playerhealth = Playerhealth + Enemyattack
            Enemyhealth = Enemyhealth + Enemyheal
            print('Enemy healed, enemy HP left: ' + str(Enemyhealth))
            print('-----------------------------------------------')
            # Playerhealth is an interger, so we use str(...) to concatenate with strings
            time.sleep(2.5)
        if Playerchoice == '2' and Enemychoice == '3':
            if Enemymiss < 70:
                Playerhealth = Playerhealth + Playerheal
                print('You healed, Player (You) HP left: ' + str(Playerhealth))
                Playerhealth = Playerhealth + Enemyattack
                print('Enemy missed you, Player (You) HP left: ' + str(Playerhealth))
                print('-----------------------------------------------')
                # Playerhealth is an interger, so we use str(...) to concatenate with strings
            else:
                Playerhealth = Playerhealth + Enemyattack
                Enemyhealth = Enemyhealth + Playerattack
                Playerhealth = Playerhealth - Enemyattack
                print('Enemy attacked you, Player (You) HP left: ' + str(Playerhealth))
                print('You healed, Player (You) HP left: ' + str(Playerhealth))
                print('-----------------------------------------------')
            time.sleep(2.5)
        #pause 2.5 seconds to show the battleground pacing
        # print round result
    if Playerhealth > 0 and Enemyhealth <= 0:
        Playerwins += 1
        print('The enemy has been beaten. You win this round!')
    elif Playerhealth <= 0 and Enemyhealth > 0:
        Enemywins += 1
        print('The enemy has taken you down. You lose!')
    else:
        print('You and the enemy has both taken each other down!')
#final results
if Playerwins > Enemywins:
    time.sleep(2)
    print('Final results: You win most or all of the rounds!!!')
elif Enemywins > Playerwins:
    print('Final results: You lose!!!')
else:
    print("Final results: It's a tie!!!")