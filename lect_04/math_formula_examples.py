from math_functions import *

def calculate_bmi(weight, height):
    """Calculate BMI."""
    return weight / (height * height)


def main():
    """Start of program."""
    bmi = calculate_bmi(100, 1.8)
    print(f"BMI: {bmi}")

    rad = 10
    volume = calculate_sphere_volume(rad)
    print(f"Volume of sphere with radius {rad}: {volume}")

    result = divide(17, 3)   # 5 r 2
    print(result)

    quotient, remainder = divide(110, 19)
    print(f"110 / 19 = {quotient} r {remainder}")


main()  # call main()