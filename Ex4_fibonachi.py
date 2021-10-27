n = int(input("n = "))

x = 1
y = 1
i = 1

for i in range(n):
    if i<2:
        print(1, end='- ')
    if i>=2:
        temp = x
        x = y
        y = y+temp
        if(i==n-1):
            print(y)
        else:
            print(y, end='- ')
        i += 1
input()