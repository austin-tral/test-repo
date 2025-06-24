from calculator import Calculator, is_even

def main():
    """
    Main function to demonstrate the Calculator class and is_even function.
    """
    # Create an instance of the Calculator
    calc = Calculator()

    print("--- Using the Calculator Class ---")

    # Demonstrate the add method
    sum_result = calc.add(15, 7)
    print(f"15 + 7 = {sum_result}")

    # Demonstrate the subtract method
    difference_result = calc.subtract(20, 8)
    print(f"20 - 8 = {difference_result}")

    # Demonstrate the multiply method
    product_result = calc.multiply(5, 6)
    print(f"5 * 6 = {product_result}")

    # Demonstrate the divide method with a valid case
    division_result = calc.divide(100, 4)
    print(f"100 / 4 = {division_result}")

    # Demonstrate handling the division by zero error
    print("\n--- Testing Division by Zero ---")
    try:
        print("Attempting to divide 10 by 0...")
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Successfully caught expected error: {e}")

    print("\n--- Using the is_even Function ---")

    # Demonstrate the is_even function
    num1 = 12
    num2 = 17
    print(f"Is {num1} even? {is_even(num1)}")
    print(f"Is {num2} even? {is_even(num2)}")


if __name__ == "__main__":
    """
    This standard Python construct ensures that the main() function is called
    only when this script is executed directly (not when imported as a module).
    """
    main()
