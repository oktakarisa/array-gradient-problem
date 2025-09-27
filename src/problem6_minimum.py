import numpy as np
from src.problem5_functions import f1, f2, f3

def find_minimum(function, x_range=(-50, 50.1, 0.1)):
    x = np.arange(*x_range)
    y = function(x)
    min_idx = np.argmin(y)
    min_x, min_y = x[min_idx], y[min_idx]

    # slopes before and after
    slope_before = (y[min_idx] - y[min_idx-1]) / (x[min_idx] - x[min_idx-1]) if min_idx > 0 else None
    slope_after = (y[min_idx+1] - y[min_idx]) / (x[min_idx+1] - x[min_idx]) if min_idx < len(x)-1 else None

    return min_x, min_y, slope_before, slope_after

def main():
    funcs = [f1, f2, f3]
    labels = ["y=x^2", "y=2x^2+2x", "y=sin(x/12)"]
    ranges = [(-50,50.1,0.1), (-50,50.1,0.1), (0,50.1,0.1)]

    for f, label, r in zip(funcs, labels, ranges):
        min_x, min_y, slope_before, slope_after = find_minimum(f, r)
        print(f"Problem 6: {label}")
        print(f"  Minimum at x={min_x}, y={min_y}")
        print(f"  Slope before: {slope_before}, Slope after: {slope_after}\n")

if __name__ == "__main__":
    main()
