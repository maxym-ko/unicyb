""" Lab2

This program calculates the value of the infinite sum, using
variables (argument, accuracy) entered by the user.

The following errors are handled:
    -incorrect argument (not in the domain, not a number)
    -incorrect accuracy (less than 0, not a number)
    -program interruption (Ctrl-C was pressed)

This program was developed by Maxym Koval (Group K-12)
"""

from math import fabs

a, b = -0.9, 0.9


def s(x: float, eps: float) -> float:
    """Calculate the value of the function for x with accuracy eps"""
    k = 5
    a_k = x
    sum_series = a_k
    x_4 = x * x * x * x
    while fabs(a_k) >= eps:
        a_k *= x_4 * (k - 4) / k
        sum_series += a_k
        k += 4
    return sum_series


def info_author():
    about_author = f"\
    Author: Koval\n\
            Maxym\n\
    Group:  K-12\n"
    print(about_author)


def main():
    print("Variant #71 \nThis program calculate the value of a function using argument and accuracy, entered by the "
          "user")
    info_author()

    try:
        x = float(input(f"Input an argument value (should be from {a} to {b}): "))
        eps = float(input("Input the accuracy of the calculation (should be positive): "))
    except ValueError:
        print("\n***** Error\nYou have input an argument value or an accuracy value that can't be "
              "represented as a number. Please, restart program and try again.")
    except KeyboardInterrupt:
        print("\n***** Error\nThe program was finished, because of pressing Ctrl-C.")
    else:
        if not (a <= x <= b):
            print("\n***** Error\nYou have input an argument that isn't in domain of a function.")
        elif eps <= 0:
            print("\n***** Error\nYou have input an accuracy that is less than 0 or equal to 0.")
        else:
            print("\n***** do calculations ... ", end="")
            result = s(x, eps)
            print("done")

            print(f"for x = {x:.6f}")
            print(f"for eps = {eps:.4E}")
            print(f"result = {result:.8f}")


main()
