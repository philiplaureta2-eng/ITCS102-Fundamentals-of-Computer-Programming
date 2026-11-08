for x in range (9):
    for y in range (9):
        if x + y == 8 or x == y :
            print("*", end = "")
        else:
            print("", end = " ")
    print()
