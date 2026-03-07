#Calculator
import time

print("The math operations are +, -, * (times), / (divide/fractions), and %. \n type q to quit and history to show history.")

while True:
    User_input = input("Enter your math equation (or something else): ") #6/3
    Math_operations = ['+', '-', '*', '/', '%']

    if User_input.lower() == 'history':
        print(User_input + '=' + str(answer))
    elif User_input.lower() == 'q' or User_input.lower() == 'quit':
        print("loading...")
        time.sleep(2)
        print("Bye bye")
        break

    op = None
    for o in Math_operations:
        if o in User_input:
            op = o
            break
            #The o is only a string from one of the operations from Math_operations
    parts = User_input.split(op)  # ex. ["2", "3"]
    if User_input.lower() == 'history':
        if answer == int(answer):
            answer = int(answer)
            print(User_input + '=' + str(answer))

        else:
            print(User_input + '=' + str(answer))
    else:
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

    if answer == int(answer):
        print(int(answer))
    else:
        print(answer)

