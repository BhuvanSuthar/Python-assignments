import math
number = float(input("Enter a number: "))

square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

print(f"\nResults for the number {number}:")
print(f"Square Root: {square_root}")
print(f"Natural Logarithm (base e): {natural_log}")
print(f"Sine (in radians): {sine_value}")
