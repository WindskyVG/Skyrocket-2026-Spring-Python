import time
print("In this game, you type a number to play. I will determine if it is odd or even.")
User_input = input("Print start to play Odd or Even Game: ")
if User_input.lower() == 'start':
    while True:
        print("type 'quit game' to exit game.")
        OoEG = input("print in a number. I will determine if it is odd or even.")
        OoEG = float(OoEG)
        number = (OoEG/2)
        if (OoEG/2) == int(number):
            OoEG = int(OoEG)
            print("the number " + str(OoEG) + " is even.")
        elif (OoEG/2) == float(number):
            print("the number " + str(OoEG) + " is odd.")
        #if OoEG.lower() == 'quit game' or OoEG.lower() == 'quit':
         #   print("Bye bye")
          #  time.sleep(1)
            #break