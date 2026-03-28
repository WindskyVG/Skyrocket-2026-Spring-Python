secret = 7

guess = int(input("猜数字: "))

if guess == secret:
    print("正确！")
elif guess > secret:
    print("太大")
else:
    print("太小")