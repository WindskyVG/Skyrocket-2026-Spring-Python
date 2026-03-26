#******
#******
#******
#******
#******
print("---------------1---------------")
for i in range(5):
    for j in range(2):
        print(' ', end='')
    for j in range(3):
        print('*', end ='')
    for j in range(3):
        print('*', end ='')
    print()

#**
#****
#******
#********
print("\n")
print("---------------2-----------------")

for i in range(5):
    for j in range(4-(i*2)):
        print('', end='')
    for j in range(i):
        print('*', end='')
    for j in range(i):
        print('*', end='')
    print()

print("\n")
print("---------------3-----------------")

#*****
#****
#***
#**
#*

for i in range(5):
    for j in range(i*2):#if this is also a 10, then it will be a 10x10 thing,but since it is i, it is upside-down
        print('', end ='') #<--this mkes a new line
    for j in range(5-i):#the i changes it
        print('*', end ='')
    for j in range(0-i):
        print('*', end ='')
    print()

print("\n")
print("---------------4-----------------")

#    **
#   ****
#  ******
# ********

for i in range(5):
    for j in range(4-i):#if this is also a 10, then it will be a 10x10 thing,but since it is 10-i, it is upside-down
        print(' ', end ='') #<--this mkes a new line
    for j in range(i):#the i changes it
        print('*', end ='')
    for j in range(i):
        print('*', end ='')
    print()

print("\n")
print("---------------5-----------------")

#   **

#  ****

# ******

#  ****

#   **

for i in range(3):
    for j in range(3-i):#if this is also a 10, then it will be a 10x10 thing,but since it is 10-i, it is upside-down
        print(' ', end ='') #<--this mkes a new line
    for j in range(i):#the i changes it
        print('*', end ='')
    for j in range(i):
        print('*', end ='')
    print("\n")
for i in range(3):
    for j in range(i):#if this is also a 10, then it will be a 10x10 thing,but since it is i, it is upside-down
        print(' ', end ='') #<--this mkes a new line
    for j in range(3-i):#the i changes it
        print('*', end ='')
    for j in range(3-i):
        print('*', end ='')
    print("\n")

print("This is my range homework!")
print("-----------------------------------------------------")