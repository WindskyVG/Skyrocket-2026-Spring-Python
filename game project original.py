import time, random
Playerwins = 0
Enemywins = 0
print('By the way you and the enemy get random health and attacks..')
for i in range(1, 6):
    time.sleep(2) #add a notificeable pause between rounds
    print('\n-------- Now starting round ' + str(i) + ' -------')#round header
    Playerhealth = random.randint(100, 150)
    Enemyhealth = random.randint(100, 150)
    Playerattack = random.randint(20, 40)
    Enemyattack = random.randint(20,40)
    # display both chracter's stats.
    print('Player (You)\n' + 'HP: ' + str(Playerhealth) + '\nAttack: ' + str(Playerattack) + '\n Player rounds winned: ' + str(Playerwins))#the \n means a new line
    print('------------------------------')
    time.sleep(2)
    print('Enemy \n' + 'HP: ' + str(Enemyhealth) + '\nAttack: ' + str(Enemyattack) + '\n Enemy rounds winned: ' + str(Enemywins))
    print('------------------------------')
    time.sleep(2)
    # combat loop
    while (Playerhealth > 0) and (Enemyhealth > 0):
        Playerhealth = Playerhealth - Enemyattack
        Enemyhealth = Enemyhealth - Playerattack
        print('The Enemy attacked you,Player (You) HP left: ' + str(Playerhealth))
        print('You attacked the enemy, Enemy HP left: ' + str(Enemyhealth))
        print('---------------------------------------------------------')
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