FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """
    a function that converts fahrenheit to celsius
    """

    f_to_c = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {f_to_c}°C")


def convert_to_fahrenheit(celsius):
    """
    a function that converts celsius to fahrenheit
    """

    c_to_f = 32 + celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{celsius}°C is {c_to_f}°F")


temp_conv = float(input("Enter the temperature to convert: "))
temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temp == "C":
    convert_to_fahrenheit(temp_conv)
elif temp == "F":
    convert_to_celsius(temp_conv)
else:
    print("Invalid temperature. Please enter a numeric value.")
