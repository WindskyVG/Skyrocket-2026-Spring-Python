for i in range(1,10):
    for j in range(i + 0, 10):
        print(i, end = ' * ')
        print(j, end = (' = ' + str(i*j)+"  "))
    print()