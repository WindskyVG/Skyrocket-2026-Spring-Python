import time, random
player_victory = 0
enmey_victory = 0
for i in range(1, 3):
    time.sleep(2)
    print('\n---------- Now Starting Round' + str(i) + '----------')
    player_life = random.randint(7, 15)
    player_attack = random.randint(3, 7)
    enmey1_life = random.randint(1, 100)
    enmey1_attack = random.randint(0, 20)
    enmey2_life = random.randint(1, 100)
    enmey2_attack = random.randint(0, 20)
    print('[Player]\n' + 'HP:' + str(player_life) + '\nAttack:' + str(player_attack))
    print('-----------------------')
    time.sleep(1)
    print('[Enmey1]\n' + 'HP:' + str(enmey1_life) + '\nAttack:' + str(enmey1_attack))
    print('-----------------------')
    time.sleep(1)
    print('[Enmey2]\n' + 'HP:' + str(enmey2_life) + '\nAttack:' + str(enmey2_attack))
    print('-----------------------')
    time.sleep(1)
    while (player_life > 0) and (enmey1_life > 0) and (enmey2_life > 0):
        choice = input("Choose who you want to attack")
        if choice == '1':
            print('You attacked enemy1')
            print('[Enmey1]\n' + 'HP:' + str(enmey1_life) + '\nAttack:' - str(player_attack))
        elif choice == '2':
            print('You attacked enemy2')
            print('[Enmey2]\n' + 'HP:' + str(enmey2_life) + '\nAttack:' - str(player_attack))
        player_life = player_life - enmey1_attack
        time.sleep(1.5)
        if player_life > 0 and enmey1_life <= 0 and enmey2_life <= 0:
            player_victory += 1
            print('The enemy is dead. You win this round!')
        elif player_life <= 0 and enmey1_life > 0 and enmey2_life > 0:
            enemy_victory += 1
            print('Oh no! The enemy took you down')
        else:
            print('Whoa! You and the enemy both went down together!')
if player_victory > enemy_victory:
    time.sleep(1)
    print('[Final Result: You win!]')
elif player_victory > enemy_victory:
    time.sleep(1)
    print('[Final Result]: You lose!')
else:
    print('[Final Result]: It is a tie!')


