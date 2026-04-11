#Calculator
import time
history = []
print("The math operations are +, -, * (times), / (divide/fractions), and %. \n type q to quit and history to show history. All other things do not work.")
User_input = input("Enter your math equation (or something else): ")  # 6/3
while True:
    Math_operations = ['+', '-', '*', '/', '%']
    other_random_stuff = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '', '^', '&', '(', ')', ',', '<', '.',
                          '>', '?', '"', "'", ';', ':', '=', '[', ']', '{', '}', '|', '`', '~']

    op = None
    for o in Math_operations:
        if o in User_input:
            op = o
            break
            # The o is only a string from one of the operations from Math_operations
    parts = User_input.split(op)  # ex. ["2", "3"]

    if User_input.lower() != 'history' and User_input != other_random_stuff:  # the '!' is equal to not
        num1 = float(parts[0].strip())
        num2 = float(parts[1].strip())
    elif User_input.lower() == 'history' and User_input == other_random_stuff:
        print("Sorry that is not available yet or a valid answer.")
        print("--------------------------------------------------")
    elif User_input.lower() == 'q' or User_input.lower() == 'quit':
        print("loading...")
        time.sleep(2)
        print("Bye bye")
        break
    else:
        print("Sorry that is not available yet or a valid answer.")

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
        answer = int(answer)
    elif answer == float(answer):
        answer = float(answer)

    if answer == int(answer) and User_input != 'history':
        print(int(answer))
    elif answer == float(answer) and User_input != 'history':
        print(answer)

    history.append(User_input + ' = ' + str(answer))
    if User_input.lower() == 'history':
        print("-----------History------------")
        print("Please ignore the last statement of your history.")
        for item in history:
            print(item)
        print("----------------------------")