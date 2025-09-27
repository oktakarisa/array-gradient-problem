import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from src.problem1_linear import generate_linear_data
from src.problem3_gradient import calculate_gradient

def plot_graphs():
    x, y = generate_linear_data()
    x_grad, grad = calculate_gradient()

    # Linear function
    plt.figure()
    plt.plot(x, y, label="y = 2x + 1")
    plt.title("Linear Function")
    plt.xlabel("x"); plt.ylabel("y")
    plt.legend()
    plt.savefig("outputs/problem4_linear.png")
    plt.close()

    # Gradient
    plt.figure()
    plt.plot(x_grad, grad, color="orange", label="Gradient")
    plt.title("Gradient of Linear Function")
    plt.xlabel("x"); plt.ylabel("dy/dx")
    plt.legend()
    plt.savefig("outputs/problem4_gradient.png")
    plt.close()

def main():
    plot_graphs()
    print("Problem 4: Plots saved to outputs/problem4_linear.png and problem4_gradient.png")

if __name__ == "__main__":
    main()
