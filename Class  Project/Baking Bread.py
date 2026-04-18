import time
teaspoon_instant_yeast = 1.5
teaspoon_salt =  1.5
teaspoon_sugar = 1.5
teaspoon_all_purpose_flour = 2.5
cups_sourdough_starter = 2
cups_lukewarm_water = 0.5
print("Hi, welcome to Baking Bread instructions")
time.sleep(1)
bread_weight = float(input("How many ounces would you like 1 bread to be: "))
serving_size = float(input("How many ounces would you like 1 serving to be: "))
guest_num = int(input("How many people would be in your party: "))
bread_num = ((guest_num*serving_size)/bread_weight)

teaspoon_instant_yeast = (teaspoon_instant_yeast*bread_num)
teaspoon_salt = (teaspoon_salt*bread_num)
teaspoon_sugar = (teaspoon_sugar*bread_num)
teaspoon_all_purpose_flour = (teaspoon_all_purpose_flour*bread_num)
cups_sourdough_starter = (cups_sourdough_starter*bread_num)
cups_lukewarm_water = (cups_lukewarm_water*bread_num)
print("----------------------\nBread number: " + str(bread_num) + "\n--------Ingredients--------\nteaspoons of instant yeast: " + str(teaspoon_instant_yeast) + "\nteaspoons of salt: " + str(teaspoon_salt) + "\nteaspoons of sugar: " + str(teaspoon_sugar) + "\ncups of sourdough starter: " + str(cups_sourdough_starter) + "\ncups of lukewarm water: " + str(cups_lukewarm_water) + "\n-----------------------------\nThank you!")