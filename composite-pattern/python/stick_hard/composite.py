class Graphic:
    def draw(self):
        """        Method to draw a shape on the canvas.

        This method is responsible for drawing a shape on the canvas using the specified parameters.
        """

        pass

class Circle(Graphic):
    def __init__(self, radius):
        """        Initialize the Circle object with a given radius.

        Args:
            radius (float): The radius of the circle.
        """

        self.radius = radius

    def draw(self):
        """        Print a message to draw a circle with a given radius.

        Args:
            self (Circle): The Circle object to be drawn.
        """

        print(f"Drawing Circle with radius {self.radius}")

class Square(Graphic):
    def __init__(self, side_length):
        """        Initialize the object with the given side length.

        Args:
            side_length (int): The length of the side of the object.
        """

        self.side_length = side_length

    def draw(self):
        """        Print a message to draw a square with a given side length.

        Args:
            self: The Square object.
        """

        print(f"Drawing Square with side length {self.side_length}")

class CompositeGraphic(Graphic):
    def __init__(self):
        """        Initialize the object with an empty list for graphics.

        This method initializes the object by creating an empty list to store graphics.

        Args:
            self: The object itself.
        """

        self.graphics = []

    def add(self, graphic):
        """
        """

        self.graphics.append(graphic)

    def draw(self):
        """        Draw method to draw all the graphics in the list.

        This method iterates through the list of graphics and calls the draw method for each graphic.

        Args:
            self (object): The instance of the class.
        """

        for graphic in self.graphics:
            graphic.draw()

# Usage
composite = CompositeGraphic()
for _ in range(500000):
    composite.add(Circle(5))

for _ in range(500000):
    composite.add(Square(4))

composite.draw()
