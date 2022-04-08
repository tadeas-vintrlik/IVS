""" @package parser
@brief Calculator input parser
@author Tadeas Vintrlik <xvintr04>

A very simple parser that serves
as an interface between the ::gui and ::math_library
"""
import re
import math_library as m

## List of all the possible operators, unsued at the moment, kept for reference
OPERATORS = ["√", "+", "-", "*", "/", "^", "!", "Fib"]
## Binary operators in `A op B` format, used in ::test_binary
OP_BINARY = ["+", "-", "*", "/", "^", "√"]
## Prefix operators `op A` format, used in ::test_prefix
OP_PREFIX = ["√"]
## Postfix operators `A op` format, used in ::test_postfix
OP_POSTFIX = ["!"]
## Functions `F(A)` format, used in ::test_function
FUNCTIONS = ["Fib"]


def is_int_float(number):
    """ @brief check if input is a valid number either integer
    or floating point format

    @param number number to check
    @return True if int or float, False otherwise
    """
    try:
        int(number)
        return True
    except ValueError:
        try:
            float(number)
            return True
        except ValueError:
            return False


def test_binary(array):
    """ @brief check if input is a valid binary expression

    `A op B` format
    @param array parsed array split by operators using ::split_elements
    @return True if valid binary expression, False otherwise
    """
    # Can't possibly be `A op B` when array has different length
    if len(array) != 3:
        return False

    # If not one of the valid binary opeators
    if array[1] not in OP_BINARY:
        return False

    # Check if first is a number
    if not is_int_float(array[0]):
        return False

    # Check if third is a number
    if not is_int_float(array[2]):
        return False

    # check if number is an integer for power
    if array[1] == "^" and ("." in array[0] or "." in array[2]):
        return False

    return True


def test_prefix(array):
    """ @brief check if input is a valid prefix expression

    `op A` format
    @param array parsed array split by operators using ::split_elements
    @return True if valid prefix expression, False otherwise
    """

    # Can't possibly be `op A` when array has different length
    if len(array) != 2:
        return False

    # If not one of the valid prefix operators
    if array[0] not in OP_PREFIX:
        return False

    # Check if second a number
    if not is_int_float(array[1]):
        return False

    return True


def test_postfix(array):
    """ @brief check if input is a valid postfix expression

    `A op` format
    @param array parsed array split by operators using ::split_elements
    @return True if valid postfix expression, False otherwise
    """
    # Can't possibly be `A op` when array has different length
    if len(array) != 2:
        return False

    # If not one of the valid prefix operators
    if array[1] not in OP_POSTFIX:
        return False

    # Check if second a number
    if not is_int_float(array[0]):
        return False

    # if floating point number
    if "." in array[0]:
        return False

    return True


def test_function(array):
    """ @brief check if input is a valid function expression

    `f(A)` format
    @param array parsed array split by operators using ::split_elements
    @return True if valid function expression, False otherwise
    """

    # Can't possibly be `f(a)` when array has different length
    if len(array) != 4:
        return False

    # If not one of the valid prefix operators
    if array[0] not in FUNCTIONS:
        return False

    # Check if third a number
    if not is_int_float(array[2]):
        return False

    # If a floating point number
    if "." in array[2]:
        return False

    # Check if second and fourth are parantheses
    if not (array[1] == "(" and array[3] == ")"):
        return False

    return True


def valid_expression(array):
    """ @brief Check if valid and computable expression in on of the
    supported formats

    Expects array to be split by operators by the ::split_elements function

    @param array field of split elements from calculator input
    @return True if valid expression, False otherwise
    """
    # Case binary
    if test_binary(array):
        return True

    # Case Prefix
    if test_prefix(array):
        return True

    # Case Postfix
    if test_postfix(array):
        return True

    # Case Function
    if test_function(array):
        return True

    return False


def join_number_operator(arr):
    """ @brief Try join minus or plus with numbers if not an operator
    @todo This function is terribly inefficient, this might not be a worry
    since it is run only in user time, so it is not noticable

    @param arr array of split input
    @return array with some elements joined
    """

    operators = 0
    for elem in arr:
        if elem in OPERATORS:
            operators += 1

    shortables = ["+", "-"]
    pop_indexes = []
    for i in range(len(arr)-1):
        # if i is - or + i+1 is a number and either there are still operators
        # left or is just in format -number or +number
        if arr[i] in shortables and is_int_float(arr[i+1])\
                and (operators > 1 or len(arr) < 3):
            pop_indexes.append(i)
            operators -= 1
            if arr[i] == "-":
                if "." in arr[i+1]:
                    arr[i+1] = str(-float(arr[i+1]))
                else:
                    arr[i+1] = str(-int(arr[i+1]))

    new = []
    for i in range(len(arr)):
        if i not in pop_indexes:
            new.append(arr[i])

    return new


def split_elements(text):
    """ @brief Split elements by operators into array

    Also removes whitespace.
    @param text input which to split
    @return array of strings split accordingly
    """
    split = re.split(r"(\+|-|\*|\/|!|\^|√|\(|\)| )", text)
    return list(filter(lambda x: x != " " and x != "", split))


def check_valid(text):
    """ @brief check if a valid (computable) input
    @param text input from the calculator entry
    @return True if valid expression, False otherwise
    """
    op_count = 0  # Number of operators

    # Split by whitespaces and all possbile operators
    split = split_elements(text)

    # empty is valid
    if len(split) == 0:
        return True

    split = join_number_operator(split)

    # If just a number alone
    if len(split) == 1:
        if is_int_float(split[0]):
            return True

    # Can't possibly have more than 4 and be valid due to the
    # nature fo the operators
    if len(split) > 4:
        return False

    for group in split:
        if len(group) == 1 and group in OPERATORS:
            op_count += 1

    # Can only compute one operator at most
    if op_count > 1:
        return False

    return valid_expression(split)


def compute_binary(array):
    """ @brief Computes a binary operator expression

    @param array parsed array split by operators using ::split_elements
    @return string the computed expression
    """
    num1 = array[0]
    operator = array[1]
    num2 = array[2]

    if operator == "+":
        if "." in num1 or "." in num2:
            return str(m.add(float(num1), float(num2)))
        else:
            return str(m.add(int(num1), int(num2)))
    elif operator == "-":
        if "." in num1 or "." in num2:
            return str(m.sub(float(num1), float(num2)))
        else:
            return str(m.sub(int(num1), int(num2)))
    elif operator == "*":
        if "." in num1 or "." in num2:
            return str(m.multiply(float(num1), float(num2)))
        else:
            return str(m.multiply(int(num1), int(num2)))
    elif operator == "/":
        try:
            if "." in num1 or "." in num2:
                return str(m.divide(float(num1), float(num2)))
            else:
                return str(m.divide(int(num1), int(num2)))
        except ZeroDivisionError:
            return "Chyba: nelze dělit nulou"
    elif operator == "^":
        try:
            return str(m.exp(int(num1), int(num2)))
        except ValueError:
            return "Chyba: záporná mocnina"
    else:  # root
        try:
            return str(m.sqrt(float(num2), int(num1)))
        except ZeroDivisionError:
            return "Chyba: nultou odmocninu nelze"
        except ValueError:
            return "Chyba: odmocnina ze záporných"


def compute_prefix(array):
    """ @brief Computes a prefix operator expression

    @param array parsed array split by operators using ::split_elements
    @return string the computed expression
    """
    num1 = array[1]
    # The only prefix operator is sqrt at the moment
    try:
        return str(m.sqrt(float(num1), 2))
    except ValueError:
        return "Chyba: odmocnina ze záporných"


def compute_postfix(array):
    """ @brief Computes a postfix operator expression

    @param array parsed array split by operators using ::split_elements
    @return string the computed expression
    """
    num1 = array[0]
    # The only postfix operator is ! at the moment
    try:
        return str(m.factorial(int(num1)))
    except ValueError:
        return "Chyba: faktoriál ze záporných"


def compute_function(array):
    """ @brief Computes a function expression

    @param array parsed array split by operators using ::split_elements
    @return string the computed expression
    """
    num1 = array[2]
    try:
        return str(m.fibonacci(int(num1)))
    except ValueError:
        return "Chyba: Fibonacci ze záporných"


def compute_solution(text):
    """ @brief Compute a solution of the expression in text

    Must be in a valid format, can be checked by ::check_valid.
    This function does no check the format itself, if in an invalid format
    it will return what it got as a paremeter.

    @param text string containing the expression to be computed
    @return the numeric result as a string
    """

    array = split_elements(text)
    array = join_number_operator(array)
    if test_binary(array):
        return compute_binary(array)

    if test_prefix(array):
        return compute_prefix(array)

    if test_postfix(array):
        return compute_postfix(array)

    if test_function(array):
        return compute_function(array)

    string = ""
    for elem in array:
        string += elem
    return string
