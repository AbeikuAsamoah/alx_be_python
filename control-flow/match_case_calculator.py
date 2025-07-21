num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        sum = num1 + num2
        print("The result is: ", sum)
    case "-":
        sub = num1 - num2
        print("The result is: ", sub)
    case "*":
        mul = num1 * num2
        print("The result is: ", mul)
    case "/":
        if num2 < 1:
            print("Cannot divide by zero")
        else:
            div = num1 / num2
            print("The result is: ", div)
