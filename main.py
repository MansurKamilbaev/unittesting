import unittest


class Calculator:
    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Division by zero is not allowed")

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y


class TestCalculatorMethods(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calculator.divide(8, 0)

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-2, 3), 1)
        self.assertEqual(self.calculator.add(0, 5), 5)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 2), 3)
        self.assertEqual(self.calculator.subtract(3, 7), -4)
        self.assertEqual(self.calculator.subtract(0, 5), -5)


if __name__ == '__main__':
    unittest.main()
