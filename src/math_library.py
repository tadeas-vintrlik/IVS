""" @package math_library
    @author: Vojtech Fiala <xfiala61>
    @brief Documentation for math library.
"""

###################################################
#              Math Functions                     #
###################################################

def factorial(number):
    """ @brief Calculate factorial of a number.
        @param number The number of which factorial to calculate.
    """
    if number < 0 or isinstance(number, float):
        raise ValueError

    result = 1
    for i in range(1, number+1):
        result *= i

    return result

def add(number, number2):
    """ @brief Add two numbers.
        @param number Operand 1.
        @param number2 Operand 2.
    """
    return number + number2

def sub(number, number2):
    """ @brief Substract two numbers.
        @param number Operand 1.
        @param number2 Operand 2.
    """
    return number - number2

def multiply(number, number2):
    """ @brief Multiply two numbers.
        @param number Operand 1.
        @param number2 Operand 2.
    """
    return number * number2

def divide(number, number2):
    """ @brief Divide two numbers.
        @param number Operand 1.
        @param number2 Operand 2.
    """
    return number / number2

def exp(number, number2):
    """ @brief Calculate exponent value of a number.
        @param number Base number.
        @param number2 The exponent.
    The base number must be a positive integer or 0.
    """
    if number2 < 0 or isinstance(number2, float):
        raise ValueError
    return pow(number, number2)

def sqrt(number, number2):
    """ @brief Calculate root value of a number.
        @param number Base number.
        @param number2 The n-th root.
    The base number must be a positive integer or 0 when number2 is even.
    """
    if ((number < 0 and number2 % 2 == 0) or isinstance(number2, float)):
        raise ValueError
    # When odd root of negative number
    if number2 % 2 != 0 and number < 0:
        return -pow(-number, 1/number2)
    else:
        return pow(number, 1/number2)

def fibonacci(number):
    """ @brief Calculate the corresponding number of fibbonaci sequence at index.
        @param number Base number.
    The base number must be a natural number.
    """
    if number < 0 or isinstance(number, float):
        raise ValueError

    if number == 0:
        return 0

    if number == 1:
        return 1

    seq = [0,1]
    result = 0
    for i in range(2,number+1):
        result = seq[i-1] + seq[i-2]
        seq.append(result)
    return result
