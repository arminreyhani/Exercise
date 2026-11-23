
import math

print("================================")
print("       SCIENTIFIC CALCULATOR")
print("================================")

while True:
    print("\nPlease select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine (Sin)")
    print("8. Cosine (Cos)")
    print("9. Tangent (Tan)")
    print("10. Logarithm (Log)")
    print("11. Natural Logarithm (Ln)")
    print("12. Factorial")
    print("13. Show Pi")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "0":
        print("Calculator closed. Goodbye!")
        break

    try:

        if choice == "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", num1 + num2)

        elif choice == "2":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", num1 - num2)

        elif choice == "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", num1 * num2)

        elif choice == "4":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error! Division by zero is not allowed.")

        elif choice == "5":
            num1 = float(input("Enter base number: "))
            num2 = float(input("Enter exponent: "))
            print("Result:", num1 ** num2)

        elif choice == "6":
            num1 = float(input("Enter a number: "))

            if num1 >= 0:
                print("Square Root:", math.sqrt(num1))
            else:
                print("Error! Negative numbers are not allowed.")

        elif choice == "7":
            angle = float(input("Enter angle in degrees: "))
            result = math.sin(math.radians(angle))
            print("Sine:", result)

        elif choice == "8":
            angle = float(input("Enter angle in degrees: "))
            result = math.cos(math.radians(angle))
            print("Cosine:", result)

        elif choice == "9":
            angle = float(input("Enter angle in degrees: "))

            if angle % 180 == 90:
                print("Error! Tangent is undefined.")
            else:
                result = math.tan(math.radians(angle))
                print("Tangent:", result)

        elif choice == "10":
            num1 = float(input("Enter a number: "))

            if num1 > 0:
                print("Logarithm:", math.log10(num1))
            else:
                print("Error! Number must be greater than zero.")

        elif choice == "11":
            num1 = float(input("Enter a number: "))

            if num1 > 0:
                print("Natural Logarithm:", math.log(num1))
            else:
                print("Error! Number must be greater than zero.")

        elif choice == "12":
            num1 = int(input("Enter a non-negative integer: "))

            if num1 >= 0:
                print("Factorial:", math.factorial(num1))
            else:
                print("Error! Negative numbers are not allowed.")

        elif choice == "13":
            print("Pi =", math.pi)

        else:
            print("Invalid choice! Please try again.")

    except ValueError:
        print("Error! Please enter a valid number.")

    except OverflowError:
        print("Error! The result is too large.")
