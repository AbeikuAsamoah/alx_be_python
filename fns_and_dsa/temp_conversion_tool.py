FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temp = float(input("Enter the temperature to convert: ").strip())
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")

else:
    try:
        c_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if c_f not in ("C", "F"):
            raise ValueError("Invalid input. Please enter C or F.")

        if c_f == "C":
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")

        elif c_f == "F":
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")

    except ValueError as e:
        print(e)
