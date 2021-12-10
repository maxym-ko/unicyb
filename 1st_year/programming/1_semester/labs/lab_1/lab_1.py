import math


def info_author():
    about_author = f"\
    Author: Koval\n\
            Maxym\n\
    Group:  K-12\n"
    print(about_author)


def domain(x: float):
    """Check if x is in the domain of the expression"""
    return (x - 5) and (x + 6) and (x + 12)


def f(x: float) -> float:
    """Calculate the value of the expression"""
    return math.cos(29 / 63) - 22 * math.e / 51 / math.pi * 10 / (x - 5) / (x + 6) + 7 * math.sin(x - 8) - 5 / (x + 12)


def f_total(x: float) -> bool and float:
    """
    Calculate the value of the expression if it is possible
    Return True if calculation is successful or False if not and the result of the calculation
    """
    if not domain(x):
        return False, None
    else:
        return True, f(x)


def main():
    print("Variant #71 \nThis program calculate an expression using variables, entered by the user")
    info_author()

    x = input("Input the value of x: ")

    try:
        x = float(x)
    except ValueError:
        print("\nwrong input \nYou have input a value of x that can't be represented as a number. Please, "
              "restart program and try again.")
    else:
        print("\n***** do calculations ... ", end="")
        success, result = f_total(x)
        print('done\n')

        print(f"for x = {x:.6f}")
        if success:
            print(f"result = {result:.6f}")
        else:
            print(
                f"result = undefined \nThe result can't be calculated because x = {x} isn't in the domain of the "
                "expression.")


main()
