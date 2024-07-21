class Calculator:
    """A class that performs arithmetic operations."""
    
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Returns the sum of two numbers.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The sum of the two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Returns the product of two numbers and prints the calculation type.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The product of the two numbers.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b