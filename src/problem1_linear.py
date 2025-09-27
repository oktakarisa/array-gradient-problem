import numpy as np

def generate_linear_data():
    x = np.arange(-50, 50.1, 0.1)
    y = 2 * x + 1
    return x, y

def main():
    x, y = generate_linear_data()
    print("Problem 1: Generated linear function y = 2x + 1")
    print(f"x shape: {x.shape}, y shape: {y.shape}")
    print(f"First 5 values: {list(zip(x[:5], y[:5]))}")

if __name__ == "__main__":
    main()
