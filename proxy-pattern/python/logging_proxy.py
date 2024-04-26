from abc import ABC, abstractmethod

# Interface for the Calculator service
class CalculatorService(ABC):
    @abstractmethod
    def add(self, x, y):
        """        Add two numbers.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The sum of x and y.
        """

        pass

    @abstractmethod
    def subtract(self, x, y):
        """        Subtract two numbers.

        This function subtracts the second number from the first number.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The result of subtracting y from x.
        """

        pass

# Real implementation of the Calculator service
class Calculator(CalculatorService):
    def add(self, x, y):
        """        Add two numbers.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The sum of x and y.
        """

        return x + y

    def subtract(self, x, y):
        """        Subtract two numbers.

        Args:
            x (int): The minuend.
            y (int): The subtrahend.

        Returns:
            int: The difference of x and y.
        """

        return x - y

# Logging Proxy for the Calculator service
class LoggingProxy(CalculatorService):
    def __init__(self, real_calculator):
        """        Initialize the instance with a real calculator object.

        Args:
            real_calculator: The real calculator object to be initialized.
        """

        self._real_calculator = real_calculator

    def _log(self, method, *args):
        """        Log the method and its arguments.

        This function logs the method name and its arguments.

        Args:
            method (str): The name of the method being logged.
            *args: Variable length argument list.
        """

        print(f"Logging: {method}({args})")

    def add(self, x, y):
        """        Perform addition operation on two numbers.

        This method logs the operation, performs the addition of two numbers, and returns the result.

        Args:
            x (int or float): The first number.
            y (int or float): The second number.

        Returns:
            int or float: The result of the addition operation.
        """

        self._log("add", x, y)
        result = self._real_calculator.add(x, y)
        print(f"Result of add operation: {result}")
        return result

    def subtract(self, x, y):
        """        Subtract two numbers.

        This method subtracts the second number from the first number and returns the result.

        Args:
            x (int or float): The first number.
            y (int or float): The second number to be subtracted from the first.

        Returns:
            int or float: The result of subtracting y from x.
        """

        self._log("subtract", x, y)
        result = self._real_calculator.subtract(x, y)
        print(f"Result of subtract operation: {result}")
        return result

# Client code
def client_code(calculator):
    """    Executes addition and subtraction operations using the provided calculator object.

    Args:
        calculator: An object that supports the add and subtract operations.
    """

    result_add = calculator.add(10, 5)
    result_subtract = calculator.subtract(20, 7)
    print("add", result_add)
    print("sub", result_subtract)

# Using the Calculator directly
# print("Using Calculator:")
real_calculator = Calculator()
# client_code(real_calculator)

# Using the LoggingProxy to add logging to the Calculator
print("\nUsing LoggingProxy:")
logging_proxy = LoggingProxy(real_calculator)
client_code(logging_proxy)