"""
main.py
--------
Entry point for running all problems (1 to 6).
Each problem is in its own script inside the src/ folder.
"""

import src.problem1_linear as p1
import src.problem2_array as p2
import src.problem3_gradient as p3
import src.problem4_plot as p4
import src.problem5_functions as p5
import src.problem6_minimum as p6

def run_all():
    print("\n=== Running Problem 1 ===")
    p1.main()

    print("\n=== Running Problem 2 ===")
    p2.main()

    print("\n=== Running Problem 3 ===")
    p3.main()

    print("\n=== Running Problem 4 ===")
    p4.main()

    print("\n=== Running Problem 5 ===")
    p5.main()

    print("\n=== Running Problem 6 ===")
    p6.main()

if __name__ == "__main__":
    run_all()
