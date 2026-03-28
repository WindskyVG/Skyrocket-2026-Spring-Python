import random

while True:
    user = input("请输入（石头/剪刀/布，输入q退出）: ")

    if user == "q":
        print("游戏结束")
        break

    if user not in ["石头", "剪刀", "布"]:
        print("输入无效，请重新输入！")
        continue

    computer = random.choice(["石头", "剪刀", "布"])
    print("电脑出的是:", computer)

    if user == computer:
        print("平局")
    elif user == "石头" and computer == "剪刀":
        print("你赢了")
    elif user == "剪刀" and computer == "布":
        print("你赢了")
    elif user == "布" and computer == "石头":
        print("你赢了")
    else:
        print("你输了")








