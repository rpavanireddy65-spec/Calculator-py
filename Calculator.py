import math

while True:
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Percentage")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a * b)

    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result:", a / b)

    elif choice == "5":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if b == 0:
            print("Error: Cannot find modulus with zero.")
        else:
            print("Result:", a % b)

    elif choice == "6":
        a = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        print("Result:", a ** b)

    elif choice == "7":
        a = float(input("Enter a number: "))

        if a < 0:
            print("Error: Square root of a negative number is not possible.")
        else:
            print("Result:", math.sqrt(a))

    elif choice == "8":
        a = float(input("Enter the number: "))
        b = float(input("Enter the percentage: "))
        print("Result:", (a * b) / 100)

    elif choice == "9":
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice. Please try again.")
