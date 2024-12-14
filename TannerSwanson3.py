import sys
from formulas import Calculator

def log_result(operator: str, values: list[float], result: float) -> None:
    with open("results.log", "a") as file:
        file.write(f"Operation: {operator}, Values: {values}, Result: {result:.2f}\n")

def main() -> None:
    try:
        if len(sys.argv) <= 2:
            sys.exit("Need to provide operator and at least two values.")
        
        operator = sys.argv[1]
        numbers = sys.argv[2:]

        try:
            numbers = [float(num) for num in numbers]
        except ValueError:
            sys.exit("All values must be numbers.")

        calculator = Calculator()

        if operator == "add":
            result = calculator.add(numbers)
        elif operator == "subtract":
            result = calculator.subtract(numbers)
        elif operator == "multiply":
            result = calculator.multiply(numbers)
        elif operator == "divide":
            result = calculator.divide(numbers)
        else:
            sys.exit("Valid operator names: add, subtract, multiply, divide.")
        
        print(f"Answer = {result:.2f}")
        log_result(operator, numbers, result)

    except ValueError as e:
        sys.exit(f"Error: {e}")
    except Exception as e:
        sys.exit(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
