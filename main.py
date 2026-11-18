
# ==========================================
# INTERACTIVE CALCULATOR & UNIT CONVERTER
# Project 01
# ==========================================


# Function to get valid numeric input
def get_number(message):

    while True:
        try:
            number = float(input(message))
            return number

        except ValueError:
            print("Invalid input! Please enter a valid number.")


# ==========================================
# CALCULATOR FUNCTIONS
# ==========================================

def calculator():

    print("\n===== BASIC CALCULATOR =====")

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:

        choice = input("Enter your choice (1-4): ")

        if choice in ["1", "2", "3", "4"]:
            break

        print("Invalid choice! Please select between 1 and 4.")

    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":

        if num2 == 0:
            print("Error! Division by zero is not allowed.")

        else:
            result = num1 / num2
            print("Result:", result)


# ==========================================
# DISTANCE CONVERTER
# ==========================================

def distance_converter():

    print("\n===== DISTANCE CONVERTER =====")

    print("1. Kilometres to Miles")
    print("2. Miles to Kilometres")

    while True:

        choice = input("Enter your choice (1-2): ")

        if choice in ["1", "2"]:
            break

        print("Invalid choice! Try again.")

    value = get_number("Enter distance: ")

    if choice == "1":

        result = value * 0.621371

        print(value, "kilometres =", round(result, 3), "miles")

    else:

        result = value / 0.621371

        print(value, "miles =", round(result, 3), "kilometres")


# ==========================================
# TEMPERATURE CONVERTER
# ==========================================

def temperature_converter():

    print("\n===== TEMPERATURE CONVERTER =====")

    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    while True:

        choice = input("Enter your choice (1-2): ")

        if choice in ["1", "2"]:
            break

        print("Invalid choice! Try again.")

    value = get_number("Enter temperature: ")

    if choice == "1":

        result = (value * 9/5) + 32

        print(value, "°C =", round(result, 2), "°F")

    else:

        result = (value - 32) * 5/9

        print(value, "°F =", round(result, 2), "°C")


# ==========================================
# CURRENCY CONVERTER
# ==========================================

def currency_converter():

    print("\n===== CURRENCY CONVERTER =====")

    print("1. INR to USD")
    print("2. USD to INR")

    # Illustrative fixed exchange rate.
    # Update this value before real-world use.
    exchange_rate = 0.011

    while True:

        choice = input("Enter your choice (1-2): ")

        if choice in ["1", "2"]:
            break

        print("Invalid choice! Try again.")

    amount = get_number("Enter amount: ")

    if choice == "1":

        result = amount * exchange_rate

        print("INR", amount, "=", "USD", round(result, 2))

    else:

        result = amount / exchange_rate

        print("USD", amount, "=", "INR", round(result, 2))


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n================================")
        print("     CALCULATOR & CONVERTER")
        print("================================")

        print("1. Basic Calculator")
        print("2. Distance Converter")
        print("3. Temperature Converter")
        print("4. Currency Converter")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":

            calculator()

        elif choice == "2":

            distance_converter()

        elif choice == "3":

            temperature_converter()

        elif choice == "4":

            currency_converter()

        elif choice == "5":

            print("\nThank you for using the application!")
            print("Goodbye!")
            break

        else:

            print("Invalid choice! Please select between 1 and 5.")


# Run the application
if __name__ == "__main__":
    main()
