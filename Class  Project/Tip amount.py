print("Hi, welcome to Sophia's Shop For Nothing,\nAll your tips given will be used for personal gain. ")
money_paid = float(input("How much money would you like to give to me for absolutely no reason?\nPlease enter your number without the money sign: "))
tip_percent = float(input("What percentage of tips would you give me? Please enter: "))
people_amount = input("How many people is here: ")
tip_each_person_amount = ((tip_percent)/100 * money_paid)
tip_amount = tip_each_person_amount * int(people_amount)
total_money = money_paid + tip_amount
print("-----------------\nSubtotal: $" + str(money_paid) + "\nTip: $" + str(tip_amount) + "\nTips each person: $" + str(tip_each_person_amount) + "\n---------------\nTotal: $" + str(total_money) + "\n-----------------\nThank you for visiting Sophia's Shop For Nothing!\nHave a good day!")