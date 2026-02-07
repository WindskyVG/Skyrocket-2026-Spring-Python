
import time

print("If you want unlimited strength and energy, you must claim the Power Stone.")
time.sleep(2)

print("If you wish to teleport anywhere in space, you must claim the Space Stone.")
time.sleep(2)

print("If you want to rewrite reality itself—no matter the cosmic laws—you must claim the Reality Stone.")
time.sleep(2)

print("If you hope to arrive at any point in time, from ancient history to the far future, you must claim the Time Stone.")
time.sleep(2)

print("If you wish to command the souls of the living and the dead, you must claim the Soul Stone.")
time.sleep(2)

print("If you dream of vast mental power and controlling anyone’s thoughts, you must claim the Mind Stone.")
time.sleep(2)

print("So… if it were up to you, which Infinity Stone would you go after?")
time.sleep(2)

print("""Please choose from the six options below:
1. Power Stone
2. Space Stone
3. Reality Stone
4. Time Stone
5. Soul Stone
6. Mind Stone""")
time.sleep(3)

answer = input("Enter the number of your choice: ")

if answer == '1':
    print("Here’s a hint: the Power Stone is locked away in the Nova Corps vault on Xandar.")
    time.sleep(3)

elif answer == '2':
    print("The Space Stone is currently in Loki’s possession.")
    time.sleep(3)

elif answer == '3':
    print("The Reality Stone (Aether) was entrusted to the Collector for safekeeping.")
    time.sleep(3)

elif answer == '4':
    print("Doctor Strange once traded the Time Stone to save Iron Man’s life.")
    time.sleep(3)

elif answer == '5':
    print("To obtain the Soul Stone, you must sacrifice someone you truly love.")
    time.sleep(3)

elif answer == '6':
    print("The Mind Stone was destroyed on Vision’s forehead by Scarlet Witch, but it can be restored with the Time Stone.")
    time.sleep(3)

else:
    print("That number doesn’t match any Infinity Stone option—try again next time!")
    time.sleep(3)

