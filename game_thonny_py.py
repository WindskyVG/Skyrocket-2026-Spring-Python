import time
import random

player_victory = 0
enemy_victory = 0
perfect_dodge_available = True   # once per game
crit_chance = 0.25               # 25% chance to double attack
miss_chance = 0.95
criticalattack_uses = 2          # two per game

for i in range(1, 4):
    print('\n------ Now Starting Round ' + str(i) + ' ------')
    time.sleep(2)

    player_life = random.randint(100, 150)
    player_attack = random.randint(30, 50)
    player_heal = random. randint (40, 50)
    enemy_life = random.randint(100, 150)
    enemy_attack = random.randint(30, 50)

    potion_uses = 2
    enemy_waits = 2

    print('[Player]')
    print('Energy:', player_life)
    print('Attack:', player_attack)
    print('----------------------------------')
    time.sleep(1)

    print('[Enemy]')
    print('Energy:', enemy_life)
    print('Attack:', enemy_attack)
    print('----------------------------------')
    time.sleep(2)

    while player_life > 0 and enemy_life > 0:
        damage = 0
        dodge_type = None

        print('\nChoose your action:')
        print('1. Attack')
        print('2. Critical Attack (x2 damage)')
        print('3. Dodge (Reduce enemy damage by 50%)')
        print('4. Perfect Dodge (Ignore attack, once per game)')
        print('5. Use Healing Potion (+40 ~ 50 Energy)')
        print('Potions left:', potion_uses)
        print('Perfect Dodge:', 'AVAILABLE' if perfect_dodge_available else 'USED')
        print('Critical Attacks left:', criticalattack_uses)

        time.sleep(0.5)

        # ===== INPUT VALIDATION (NO TURN SKIP) =====
        while True:
            choice = input('Enter 1 / 2 / 3 / 4 / 5: ')

            if choice not in ['1', '2', '3', '4', '5']:
                print('Invalid input!')
                continue

            if choice == '2' and criticalattack_uses == 0:
                print('Invalid input! No critical attacks left.')
                continue

            if choice == '4' and not perfect_dodge_available:
                print('Invalid input! Perfect dodge already used.')
                continue

            if choice == '5' and potion_uses == 0:
                print('Invalid input! No potions left.')
                continue

            break   # valid choice

        time.sleep(1)

        # ===== PLAYER TURN =====
        if choice == '1':
            damage = player_attack        
            if random.random() < crit_chance:
                damage *= 1.5
                print('You got REALLY good luck today! Damage x1.5!')
            if random. random() > miss_chance:
                damage = 0
                print('Uh oh! You missed your shot! Zero damage.')

            enemy_life -= damage
            print('You attacked! Damage:', damage)
            print('Enemy energy left:', enemy_life)

        elif choice == '2':
            damage = player_attack * 2
            criticalattack_uses -= 1
            enemy_life -= damage
            print('CRITICAL ATTACK! Damage:', damage)
            print('Enemy energy left:', enemy_life)

        elif choice == '3':
            dodge_type = 'partial'
            print('You prepare a partial dodge!')

        elif choice == '4':
            dodge_type = 'perfect'
            print('You prepare a PERFECT dodge!')

        elif choice == '5':
            player_life += player_heal
            potion_uses -= 1
            print('You used a healing potion! +',player_heal, 'energy')
            print('Player energy now:', player_life)

        time.sleep(1)

        # ===== ENEMY TURN =====
        if enemy_life > 0:
            print('\nEnemy chooses an action...')
            time.sleep(1)

            if enemy_waits > 0:
                enemy_action = random.choice(['attack', 'dodge', 'wait'])
            else:
                enemy_action = random.choice(['attack', 'dodge'])

            if enemy_action == 'attack':
                print('Enemy attacks!')

                if dodge_type == 'perfect':
                    print('PERFECT DODGE! No damage taken.')
                    perfect_dodge_available = False

                elif dodge_type == 'partial':
                    reduced_damage = enemy_attack // 2
                    player_life -= reduced_damage
                    print('Partial dodge! Damage reduced to', reduced_damage)
                    print('Player energy left:', player_life)

                else:
                    player_life -= enemy_attack
                    print('You were hit!')
                    print('Player energy left:', player_life)

            elif enemy_action == 'dodge':
                print('Enemy is dodging this turn.')

            elif enemy_action == 'wait':
                enemy_waits -= 1
                print('Enemy hesitates and does nothing.')
                print('Enemy waits left this round:', enemy_waits)

        print('----------------------------------')
        time.sleep(2)

    # ===== ROUND RESULT =====
    if player_life > 0 and enemy_life <= 0:
        player_victory += 1
        print('You win this round!')
    elif enemy_life > 0 and player_life <= 0:
        enemy_victory += 1
        print('You lost this round!')
    else:
        print("It's a draw!")

    time.sleep(2)

print('\n====== FINAL RESULT ======')
time.sleep(2)

if player_victory > enemy_victory:
    print('You win the game!')
elif enemy_victory > player_victory:
    print('You lose the game!')
else:
    print("It's a tie!")
