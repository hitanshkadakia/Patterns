def arrow(n):
    for x in range(n):
        if x == n-1:
            print( (2*n) * "*" , end="")
            print( (x+1) * "*")
        else:
            print( (2*n) * " " , end="")
            print( (x+1) * "*")
    for y in range(n-1,0,-1):
        print( (2*n) * " ", end="")
        print(y * "*")

arrow(5)