def calculate(operation: str, num1: float, num2: float) -> float:
    """Perform one arithmetic operation and return the result."""
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                raise ZeroDivisionError("Oops, you can't divide by zero.")
            return num1 / num2
        case _:
            raise ValueError("Please choose +, -, *, or /.")


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Oh gosh, that doesn't look like a number! Please try again.")


def main() -> None:
    print("Hey there! You found my calculator.")
    print("It can help you add (+), subtract (-), multiply (*), or divide (/).")

    while True:
        operation = input("Which operation would you like to use? ").strip()
        if operation not in ("+", "-", "*", "/"):
            print("Oh no, I don't recognize that one. Please choose +, -, *, or /!")
            continue

        num1 = get_number("What's the first number? ")
        num2 = get_number("And what's the second number? ")

        try:
            result = calculate(operation, num1, num2)
            print(f"Your answer is {result:g}.")
        except ZeroDivisionError as error:
            print(error)

        again = input("Would you like to do another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for stopping by. Have a great day!")
            break


if __name__ == "__main__":
    main()
        
