def calculator():
    print("Welcome to the Python Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        # Get user choice
        choice = int(input("Enter the number of the operation you'd like to perform (1-4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please choose a number between 1 and 4.")
            return

        # Get numbers from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform calculation
        if choice == 1:
            print(f"The result is: {num1 + num2}")
        elif choice == 2:
            print(f"The result is: {num1 - num2}")
        elif choice == 3:
            print(f"The result is: {num1 * num2}")
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"The result is: {num1 / num2}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
