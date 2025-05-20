def calculator():
    print("=== Simple Calculator ===")
    
    while True:
        try:
            # Get user input
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Operation menu
            print("\nChoose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Exit")

            choice = input("Enter choice (1/2/3/4/5): ")

            if choice == '5':
                print("Thank you for using the calculator. Goodbye!")
                break

            if choice == '1':
                result = num1 + num2
                operation = '+'
            elif choice == '2':
                result = num1 - num2
                operation = '-'
            elif choice == '3':
                result = num1 * num2
                operation = '*'
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
                operation = '/'
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
                continue

            # Display result with 2 decimal places
            print(f"Result: {num1} {operation} {num2} = {result:.2f}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

# Run the calculator
calculator()

