
PI = 3.141592653589793

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sin(x):
    x = x * PI / 180
    result = 0
    for i in range(10):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return result

def cos(x):
    x = x * PI / 180
    result = 0
    for i in range(10):
        result += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    return result

def log(x):
    if x <= 0:
        raise ValueError
    y = (x - 1) / (x + 1)
    result = 0
    for i in range(100):
        result += (y ** (2 * i + 1)) / (2 * i + 1)
    return 2 * result

while True:
    print("\nScientific Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Log (base 10)")
    print("11. Natural Log (ln)")
    print("12. Factorial")
    print("13. Pi")
    print("0. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "0":
            print("Calculator closed.")
            break

        elif choice == "1":
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
                print("Cannot divide by zero.")
            else:
                print("Result:", a / b)

        elif choice == "5":
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result:", a ** b)

        elif choice == "6":
            a = float(input("Enter number: "))
            if a < 0:
                print("Cannot calculate square root of a negative number.")
            else:
                print("Result:", a ** 0.5)

        elif choice == "7":
            a = float(input("Enter angle in degrees: "))
            print("Result:", sin(a))

        elif choice == "8":
            a = float(input("Enter angle in degrees: "))
            print("Result:", cos(a))

        elif choice == "9":
            a = float(input("Enter angle in degrees: "))
            if a % 180 == 90:
                print("Undefined result.")
            else:
                print("Result:", sin(a) / cos(a))

        elif choice == "10":
            a = float(input("Enter number: "))
            print("Result:", log(a) / log(10))

        elif choice == "11":
            a = float(input("Enter number: "))
            print("Result:", log(a))

        elif choice == "12":
            a = float(input("Enter a non-negative integer: "))
            if a < 0 or a != int(a):
                print("Factorial requires a non-negative integer.")
            else:
                print("Result:", factorial(int(a)))

        elif choice == "13":
            print("Pi =", PI)

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
