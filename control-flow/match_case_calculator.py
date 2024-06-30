# match_case_calculator.py


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")


match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
    case _:  # default case for invalid operation
        print("Invalid operation. Please try again.")
        result = None

# Output the result
if result is not None:
    print(f"The result is {result}.")