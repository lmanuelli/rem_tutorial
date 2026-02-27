# This is your first Python script!
# Lines starting with '#' are comments — Python ignores them.
# They're here to explain what the code does.

# 'import' brings in an external library so we can use its tools.
# NumPy is a library for working with numbers and arrays.
import numpy as np


def main():
    # --- Hello, World! ---
    # 'print' displays text (or values) to the terminal.
    print("Hello, world!")

    # --- A tiny NumPy demo ---
    # Create a 1-dimensional array of five numbers.
    # Think of it like a column in a spreadsheet.
    data = np.array([10, 20, 30, 40, 50])

    # Print the array itself.
    print("Data array:", data)

    # NumPy can compute statistics on the array in one line.
    print("Mean of data:", data.mean())


# This block runs only when you execute the file directly
# (e.g., `python -m rem.examples.hello_world`).
# It won't run if another file imports this one.
if __name__ == "__main__":
    main()
