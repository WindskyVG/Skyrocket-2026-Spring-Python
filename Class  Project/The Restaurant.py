one_burger = 20
one_fry_pack = 4
one_drink = 3
print("There is a discount, if you spend 20 dollars or more, your total price will get $3 off.")
print("--------------\nBurger price: $20\nFries pack price: $4\nDrink price: $3\n----------------------")
Burger_order_number = int(input("Hi, please enter the number of burgers you would like: "))
burger_price = (one_burger*Burger_order_number)
Fry_pack_order_number = int(input("Enter the number of fry packs you would like: "))
fry_pack_price = (one_fry_pack*Fry_pack_order_number)
Drink_order_number = int(input("Please enter the number of drinks you would like: "))
drink_price = (one_drink*Drink_order_number)
Order_price = (burger_price + fry_pack_price + drink_price)
print("This is your order price: \n-------------------------\nFries pack price: $" + str(fry_pack_price) + "\nBurger price: $" + str(burger_price) + "\nDrink price: $" + str(drink_price) + "\n--------------------------\nsubtotal: $" + str(Order_price))
if Order_price >= 20:
    Order_price = Order_price-3
    print("---------------------------\nDiscount = -$3\nTotal price: $" + str(Order_price))
else:
    print("---------------------------\nDiscount = -$0\nTotal price: $" + str(Order_price))
print("Thank you for coming at this restaurant!\nBye!")