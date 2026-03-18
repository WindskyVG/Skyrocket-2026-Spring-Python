#Calculator
import time
answer = None
history = []
print("The math operations are +, -, * (times), / (divide/fractions), and %. \n type q to quit and history to show history.")

while True:
    User_input = input("Enter your math equation (or something else): ") #6/3
    Math_operations = ['+', '-', '*', '/', '%']

    op = None
    for o in Math_operations:
        if o in User_input:
            op = o
            break
            #The o is only a string from one of the operations from Math_operations
    parts = User_input.split(op)  # ex. ["2", "3"]

    if User_input.lower() == 'q' or User_input.lower() == 'quit':
        print("loading...")
        time.sleep(2)
        print("Bye bye")
        break

    elif User_input != 'history':#the '!' is equal to not
        num1 = float(parts[0].strip())
        num2 = float(parts[1].strip())

    if op == '%':
        print("The answer is: ")
        answer = num1 % num2
    elif op == '*':
        print("The answer is: ")
        answer = num1 * num2
    elif op == '/':
        print("The answer is: ")
        answer = num1 / num2
    elif op == '+':
        print("The answer is: ")
        answer = num1 + num2
    elif op == '-':
        print("The answer is: ")
        answer = num1 - num2

    if answer == int(answer) and answer != None:
        print(int(answer))
    elif answer == float(answer) and answer != None:
        print(answer)

    history.append(User_input + ' = ' + str(answer))
    if User_input == 'history':
        print("-----------History------------")
        print("Please ignore the last statement of your history.")
        for item in history:
            print(item)
        print("------------------------------")

    if answer == None and User_input == 'history':
        for a in answer:
            print("Sorry that is not available yet or a valid answer.")
            print("--------------------------------------------------")