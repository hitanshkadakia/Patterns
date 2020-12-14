for row in range(0, 7):
    for column in range(0, 7):
        if(((column == 1 or column == 5) and row != 6) or (row == 6 and column > 1 and column < 5)):
            print("*", end="")
        else:
            print(" ", end="")
    print()