import math

class Shape:
    """A base class representing a generic shape."""

    def area(self):
        """
        Calculates the area of the shape.
        This method should be overridden by derived classes.
        """
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    """A class representing a rectangle, inheriting from Shape."""

    def __init__(self, length, width):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """A class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """
        Initializes a new instance of the Circle class.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)
