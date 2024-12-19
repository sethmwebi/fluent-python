import random

# Define the number of floating-point numbers
num_floats = 10_000_000

# File to store the numbers
output_file = "floating_point_numbers.txt"

# Generate and save the numbers
with open(output_file, "w") as f:
    for _ in range(num_floats):
        f.write(f"{random.uniform(-1e6, 1e6)}\n")

print(f"{num_floats} floating point numbers have been written to {output_file}.")
