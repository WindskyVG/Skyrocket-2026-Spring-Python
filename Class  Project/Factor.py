Factors = []
while True:
    Number = int(input("Enter a number to factor: "))
    for i in range(1, (Number + 1)):
        if Number % i == 0:
            Factors.append(i)
    print("Here are the Factors: ")
    print(Factors)
    Factors = []
