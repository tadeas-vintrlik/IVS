""" @package math_library_tests
    @author: Vojtech Fiala <xfiala61>
    @brief Documentation for math library tests.
"""
import unittest
from math_library import add, sub, multiply, divide
from math_library import exp, sqrt, factorial, fibonacci

class TestStringMethods(unittest.TestCase):
    """ @brief Test class to run the tests.
        @param unittest.TestCase Used to get access to test methods.
    """

    def test_addition(self):
        """ @brief Method to test the addition (+).
            @param self Self object.
        """
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(5, 15009), 15014)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, -5), -5)
        self.assertEqual(add(-5, 0), -5)
        self.assertEqual(add(-5, -5), -10)
        self.assertEqual(add(0.5, 5.8), 6.3)

    def test_substraction(self):
        """ @brief Method to test the substraction (-).
            @param self Self object.
        """
        self.assertEqual(sub(5, 5), 0)
        self.assertEqual(sub(5, 15009), -15004)
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(0, -5), 5)
        self.assertEqual(sub(-5, 0), -5)
        self.assertEqual(sub(-5, -5), 0)
        self.assertEqual(sub(0.5, 5.8), -5.3)


    def test_multiplication(self):
        """ @brief Method to test the multiplication (*).
            @param self Self object.
        """
        self.assertEqual(multiply(5, 5), 25)
        self.assertEqual(multiply(5, 15009), 75045)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(0, -5), 0)
        self.assertEqual(multiply(-54654564, 0), 0)
        self.assertEqual(multiply(-5, -5), 25)
        self.assertEqual(multiply(-5, 5), -25)
        self.assertEqual(multiply(0.5, 5.8), 2.9)

    def test_division(self):
        """ @brief Method to test the division (/).
            @param self Self object.
        """
        self.assertEqual(divide(5, 5), 1)
        self.assertEqual(divide(5, 100), 0.05)
        self.assertRaises(ZeroDivisionError, divide, 0, 0)
        self.assertRaises(ZeroDivisionError, divide, -5, 0)
        self.assertEqual(divide(0, -5), 0)
        self.assertEqual(divide(-5, -5), 1)
        self.assertEqual(divide(-5, 5), -1)
        self.assertEqual(divide(8.5, 0.5), 17)

    def test_exp(self):
        """ @brief Method to test the exponent (^).
            @param self Self object.

        The exponent can only be a natural number, which includes 0.
        """
        self.assertEqual(exp(5, 5), 3125)
        self.assertEqual(exp(5, 2), 25)
        self.assertEqual(exp(0, 5), 0)
        self.assertEqual(exp(5, 0), 1)
        self.assertEqual(exp(-5, 5), -3125)
        self.assertRaises(ValueError, exp, 9, 0.5)
        self.assertEqual(exp(2, 31), 2147483648)
        self.assertRaises(ValueError, exp, 654, -5)

    def test_sqrt(self):
        """ @brief Method to test the root (sqrt).
            @param self Self object.
        The root function doesn't support imaginary numbers.
        The operand must be a real number.
        This function supports n-th root. The 'n' can be any integer.
        """
        self.assertEqual(sqrt(9, 2), 3)
        self.assertEqual(sqrt(27, 3), 3)
        self.assertEqual(sqrt(0, 5), 0)
        self.assertEqual(sqrt(1, 5), 1)
        self.assertEqual(sqrt(1, -5), 1)
        self.assertRaises(ZeroDivisionError, sqrt, 5, 0)
        self.assertRaises(ValueError, sqrt, -5, 0)
        self.assertEqual(sqrt(5, -1), 0.2)
        self.assertEqual(sqrt(9, 1), 9)


    def test_fact(self):
        """ @brief Method to test the factorial (!)
            @param self Self object.
        Factorial operand can be any integer higher than 0.
        """
        self.assertEqual(factorial(9), 362880)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertRaises(ValueError, factorial, -1)
        self.assertRaises(ValueError, factorial, 5.5)

    def test_fibonacci(self):
        """ @brief Method to test the fibonacci sequence calculator.
            @param self Self object.
        The operand can be any natural number.
        """

        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(11), 89)
        self.assertEqual(fibonacci(50), 12586269025)
        self.assertRaises(ValueError, fibonacci, -5)
        self.assertRaises(ValueError, fibonacci, 0.5)


if __name__ == '__main__':
    unittest.main()
