m = int(input("m = "))
n = int(input("n = "))

def multiply(m , n):
    for i in range(1,m+1):
        for j in range(1,n+1):
            print(i*j,end= "  ")
        print()
multiply(m,n)