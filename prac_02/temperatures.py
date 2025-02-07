def main():
    print("Temperature Converter")
    choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? ").upper()

    if choice == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f}°C is {fahrenheit:.2f}°F")

    elif choice == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F is {celsius:.2f}°C")

    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


main()