"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""

    return num1 + num2


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return num1 - num2


def multiply(num1, num2):
    """Multiply the two inputs together."""

    return num1 * num2


def divide(num1, num2):
    """Divide the first input by the second and return the result."""

    return num1 / num2


def square(num1):
    """Return the square of the input. To use type square()"""

    return num1 ** 2


def cube(num1):
    """Return the cube of the input. To use type cube()"""

    return num1 ** 3


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value. To use type pow()"""

    return num1 ** num2


def mod(num1, num2):
    """Return the remainder of num1 / num2. To use type mod()"""

    return num1 % num2

def add_mult(num1, num2, num3):
    """Adds the first 2 numbers, then multiplies the answer with the third.

    Given the syntax x+ num1 num2 num3
    """

    return multiply(add(num1, num2), num3)

def add_cubes(num1, num2):
    """Adds together the cubes of num1 and num2.

    Given the syntax cubes+ num1 num2
    """

    return add(cube(num1), cube(num2))
