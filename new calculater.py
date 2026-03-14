history = []

while True:
    try:
        result = int(input("enter first number: "))
        break
    except ValueError:
        print("Invalid input, please enter a number.")

while True:

    print("\n====== Calculator ======")
    print("Current result:", result)
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. History")
    print("6. Clear result")
    print("q. Quit")

    choice = input("Choose: ")

    if choice == "q":
        break

    elif choice == "5":
        print("\n--- History ---")
        for item in history:
            print(item)
        continue

    elif choice == "6":
        print("Result cleared.")
        result = int(input("enter first number: "))


    if choice == "1":
        operator = "+"
    elif choice == "2":
        operator = "-"
    elif choice == "3":
        operator = "*"
    elif choice == "4":
        operator = "/"
    else:
        print("invalid choice")
        continue

    while True:
        try:
            secondnum = int(input("enter second number: "))
            break
        except ValueError:
            print("Invalid input please enter a number.")

    first = result

    if operator == "+":
        result = result + secondnum
    elif operator == "-":
        result = result - secondnum
    elif operator == "*":
        result = result * secondnum
    elif operator == "/":
        result = result / secondnum

    history.append(f"{first} {operator} {secondnum} = {result}")

    print("result:", result)