

for x in range (9):
    for y in range (9):
        if x + y == 4 or y - x == -4 or x + y == 12 or x - y == -4 :
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

