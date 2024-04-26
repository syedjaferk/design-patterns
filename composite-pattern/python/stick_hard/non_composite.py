class Circle:
    def __init__(self, radius):
        """        Initialize the Circle object with a given radius.

        Args:
            radius (float): The radius of the circle.
        """

        self.radius = radius

    def draw(self):
        """        Print a message to draw a circle with a given radius.

        This method prints a message to draw a circle with the specified radius.

        Args:
            self (Circle): The Circle object itself.
        """

        print(f"Drawing Circle with radius {self.radius}")

class Square:
    def __init__(self, side_length):
        """        Initialize the side length of a square.

        Args:
            side_length (int): The length of the side of the square.
        """

        self.side_length = side_length

    def draw(self):
        """        Print a message to draw a square with a given side length.

        Args:
            self: The Square object.
        """

        print(f"Drawing Square with side length {self.side_length}")

# Usage
circles = [Circle(5) for _ in range(1000000)]
squares = [Square(4) for _ in range(1000000)]

for circle in circles:
    circle.draw()

for square in squares:
    square.draw()
