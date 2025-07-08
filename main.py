from calculator import Calculator, is_even, AdvancedCalculator

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

    print("\n--- Using the AdvancedCalculator Class ---")
    adv_calc = AdvancedCalculator()

    # Demonstrate the power method
    power_result = adv_calc.power(3, 4)
    print(f"3 to the power of 4 = {power_result}")

    power_result_neg_base = adv_calc.power(-2, 3)
    print(f"-2 to the power of 3 = {power_result_neg_base}")

    # Demonstrate the sqrt method
    sqrt_result = adv_calc.sqrt(16)
    print(f"Square root of 16 = {sqrt_result}")

    sqrt_result_float = adv_calc.sqrt(2)
    print(f"Square root of 2 = {sqrt_result_float:.4f}") # Formatting for readability

    # Demonstrate handling the sqrt of a negative number
    print("\n--- Testing Square Root of a Negative Number ---")
    try:
        print("Attempting to calculate square root of -9...")
        adv_calc.sqrt(-9)
    except ValueError as e:
        print(f"Successfully caught expected error: {e}")
