while True:
    User_input1 = (input("please enter your first number"))
    User_input2 = input("please enter your operation")
    User_input3 = (input("please enter your second number"))

    if User_input2 == "+":
        result = intUser_input1 + intUser_input3
    elif User_input2 == "-":
        result = intUser_input1 - intUser_input3
    elif User_input2 == "*":
        result = intUser_input1 * intUser_input3
    elif User_input2 == "/":
        result = intUser_input1 / intUser_input3
    elif User_input1 == ("q") or User_input2 == ("q") or User_input3 == ("q"):
        break
    print(result)