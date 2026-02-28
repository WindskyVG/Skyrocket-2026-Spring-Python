#Calculator

while True:

    User_input = input("Enter your math equation. (The math equation must be only 1 math operation and 2 numbers): ").strip()

    if User_input.lower() == 'q' or 'quit':
        break

    Math_operations = ['+', '-', '*', '/', '%']
    op = None
    for o in Math_operations:
        if o in User_input:
            op = o
            break

    parts = User_input.split(op) # ["2", "3"]
    num1 = float(parts[0].strip())
    num2 = float(parts[1].strip())

    if op == '+':
       print("The answer is: ")
       answer = num1 + num2
    elif op == '-':
       print("The answer is: ")
       answer = num1 - num2
    elif op == '*':
       print("The answer is: ")
       answer = num1 * num2
    elif op == '/':
        print("The answer is: ")
        answer = num1 / num2
    elif op == '%':
        print("The answer is: ")
        answer = num1 % num2
    else:
        print("Sorry, that feature is unavailable. Try again.")


    if answer == int(answer):
        print(int(answer))
    else:
        print(answer)