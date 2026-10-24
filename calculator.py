# Project 1: Interactive Calculator & Unit Converter

# Conversion factors
CONVERSION_FACTORS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462
}


# Function to read a valid number
def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


# Arithmetic functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


# Unit conversion functions
def km_to_miles(km):
    return km * CONVERSION_FACTORS["km_to_miles"]


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def kg_to_pounds(kg):
    return kg * CONVERSION_FACTORS["kg_to_pounds"]


# Main function
def main():
    while True:
        print("\n===== Calculator & Unit Converter =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Kilometers to Miles")
        print("6. Celsius to Fahrenheit")
        print("7. Kilograms to Pounds")
        print("8. Quit")

        choice = input("Choose an option (1-8): ").strip()

        if choice == "8":
            print("Goodbye!")
            break

        elif choice in ("1", "2", "3", "4"):
            a = read_number("Enter first number: ")
            b = read_number("Enter second number: ")

            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            else:
                result = divide(a, b)

            print("Result:", result)

        elif choice == "5":
            km = read_number("Enter kilometers: ")
            print(f"Result: {km_to_miles(km):.3f} miles")

        elif choice == "6":
            celsius = read_number("Enter temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} Fahrenheit")

        elif choice == "7":
            kg = read_number("Enter weight in kilograms: ")
            print(f"Result: {kg_to_pounds(kg):.3f} pounds")

        else:
            print("Invalid choice! Please select from 1 to 8.")


if __name__ == "__main__":
    main()