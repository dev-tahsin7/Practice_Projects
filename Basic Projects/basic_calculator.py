x = int(input("Enter First Number: "))
xy = input("Enter Oparator: ")
y = int(input("Enter Second Number: "))

if xy == "+":
    print(x+y)
elif xy == "-":
    print(x-y)
elif xy == "*":
    print(x*y)
elif xy == "/":
    print(x/y)
else:
    print("Invalid Oparator!")
