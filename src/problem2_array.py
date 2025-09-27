import numpy as np
from src.problem1_linear import generate_linear_data

def combine_arrays():
    x, y = generate_linear_data()
    return np.column_stack((x, y))

def main():
    arr = combine_arrays()
    print("Problem 2: Combined x and y into array (shape:", arr.shape, ")")
    print(arr[:5])  # preview first 5 rows

if __name__ == "__main__":
    main()
