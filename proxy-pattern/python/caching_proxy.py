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
        """        Perform addition of two numbers.

        This function takes two numbers as input and returns their sum.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The sum of the input numbers.
        """

        print("Performing add operation")
        return x + y

    def subtract(self, x, y):
        """        Perform subtraction of two numbers.

        This function performs the subtraction operation on two numbers and returns the result.

        Args:
            x (int or float): The first number.
            y (int or float): The second number.

        Returns:
            int or float: The result of subtracting y from x.
        """

        print("Performing subtract operation")
        return x - y

# Caching Proxy for the Calculator service
class CachingProxy(CalculatorService):
    def __init__(self, real_calculator):
        """        Initialize the CalculatorCache object with a real calculator.

        This method initializes the CalculatorCache object with a real calculator and an empty cache.

        Args:
            real_calculator (Calculator): An instance of the real calculator to be aggregated.
        """

        self._real_calculator = real_calculator #aggregation
        self._cache = {}

    def add(self, x, y):
        """        Add two numbers and cache the result for future use.

        This method adds two numbers and caches the result for future use to improve performance by avoiding redundant calculations.

        Args:
            x (int): The first number to be added.
            y (int): The second number to be added.

        Returns:
            int: The sum of the input numbers.
        """

        key = f"add:{x}:{y}"
        if key not in self._cache:
            result = self._real_calculator.add(x, y) # execute
            self._cache[key] = result #store
            print(f"Caching result for add({x}, {y}): {result}")
        else:
            print(f"Using cached result for add({x}, {y}): {self._cache[key]}")
        return self._cache[key]

    def subtract(self, x, y):
        """        Subtract two numbers and cache the result for future use.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The result of subtracting x from y.
        """

        key = f"subtract:{x}:{y}"
        if key not in self._cache:
            result = self._real_calculator.subtract(x, y)
            self._cache[key] = result
            print(f"Caching result for subtract({x}, {y}): {result}")
        else:
            print(f"Using cached result for subtract({x}, {y}): {self._cache[key]}")
        return self._cache[key]

# Client code
def client_code(calculator):
    """    Client code to perform addition and subtraction operations using a calculator.

    Args:
        calculator (Calculator): An instance of the Calculator class.
    """

    result_add1 = calculator.add(10, 5)
    result_add2 = calculator.add(10, 5)  # This should use the cached result
    result_subtract1 = calculator.subtract(20, 7)
    result_subtract2 = calculator.subtract(20, 7)  # This should use the cached result

# Using the Calculator directly
print("Using Calculator:")
real_calculator = Calculator()
# client_code(real_calculator)

# Using the CachingProxy to add caching to the Calculator
print("\nUsing CachingProxy:")
caching_proxy = CachingProxy(real_calculator)
client_code(caching_proxy)
