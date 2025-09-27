import numpy as np
from src.problem1_linear import generate_linear_data

def calculate_gradient():
    x, y = generate_linear_data()
    dx = np.diff(x)
    dy = np.diff(y)
    gradient = dy / dx
    return x[:-1], gradient

def main():
    x, gradient = calculate_gradient()
    print("Problem 3: Computed gradient of y = 2x + 1")
    print(f"Gradient shape: {gradient.shape}")
    print("First 5 gradients:", gradient[:5])

if __name__ == "__main__":
    main()
