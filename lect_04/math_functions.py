import math

def calculate_sphere_volume(radius):
    """Return the volume of sphere."""
    return 4 / 3 * math.pi * radius * radius * radius

def divide(number, divisor):
    """Return integer quotient and remainder"""
    quotient = number // divisor   # int division
    remainder = number % divisor
    return quotient, remainder