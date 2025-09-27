import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def compute_gradient(function, x_range=(-50, 50.1, 0.1)):
    x = np.arange(*x_range)
    y = function(x)
    dx = np.diff(x)
    dy = np.diff(y)
    gradient = dy / dx
    return np.column_stack((x, y)), gradient

def f1(x): return x**2
def f2(x): return 2*x**2 + 2*x
def f3(x): return np.sin(x/12)

def plot_functions():
    funcs = [f1, f2, f3]
    labels = ["x2", "2x2+2x", "sin(x/12)"]
    filenames = ["outputs/problem5_x2.png",
                 "outputs/problem5_2x2_2x.png",
                 "outputs/problem5_sin.png"]
    ranges = [(-50, 50.1, 0.1), (-50, 50.1, 0.1), (0, 50.1, 0.1)]

    for f, label, fname, r in zip(funcs, labels, filenames, ranges):
        arr, grad = compute_gradient(f, r)
        x = arr[:,0]; y = arr[:,1]
        plt.figure()
        plt.plot(x, y, label=f"y = {label}")
        plt.title(f"Function: y = {label}")
        plt.xlabel("x"); plt.ylabel("y")
        plt.legend()
        plt.savefig(fname)
        plt.close()

def main():
    plot_functions()
    print("Problem 5: Function plots saved to outputs/problem5_x2.png, problem5_2x2_2x.png, problem5_sin.png")

if __name__ == "__main__":
    main()
