import time
Sophia_task = []
password = "wrong"
correct_password = "Foxesare123happy"
Username = "Sophia"
sign_in = input("Enter your login name: ")
if sign_in == Username:
    print("Welcome Sophia")
else:
    print("wrong")
password = input("Enter your password: ")
if password == correct_password:
    print("Welcome Sophia.\nLogin successful.")
else:
    print("wrong")
    