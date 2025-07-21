number = int(input("Enter a number to see it's multiplication table: "))
x = 1
for x in range(1, 11):
    mul = number * x
    print(number, "*", x, "=", mul)
