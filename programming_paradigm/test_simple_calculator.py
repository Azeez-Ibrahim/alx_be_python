import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(100, 11), 111)
        self.assertEqual(self.calc.add(50, -25), 25)
        self.assertEqual(self.calc.add(-1, -3), -4)
    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(100, 11), 89)
        self.assertEqual(self.calc.subtract(50, -25), 75)
        self.assertEqual(self.calc.subtract(-1, -3), 2)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(100, 11), 1100)
        self.assertEqual(self.calc.multiply(50, -25), -1250)
        self.assertEqual(self.calc.multiply(-1, -3), 3)
        self.assertEqual(self.calc.multiply(1, 1.5), 1.5)
    
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(20, 2), 10)
        self.assertEqual(self.calc.divide(100, 5), 20)
        self.assertEqual(self.calc.divide(50, -25), -2)
        self.assertEqual(self.calc.divide(-3, -3), 1)
        self.assertEqual(self.calc.divide(2.5, 5), 0.5)
        self.assertEqual(self.calc.divide(2.5, 0), None)
