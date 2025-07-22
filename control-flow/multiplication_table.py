number = int(input("Enter a number to see its multiplication table: "))
for x in range(1, 11):
    mul = number * x
    print(f"{number} * {x} = {mul}")
