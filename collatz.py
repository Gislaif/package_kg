x = int(input("Enter a number from 0 to 100: "))
while x !=1:
    if x>100:
        print(f"{x} is upper 100. Please, type a number 0 to 100")
    elif x % 2==0:
        print(x/2)
        x=x/2
    else:
        print((3*x)+1)
        x=3*x+1
