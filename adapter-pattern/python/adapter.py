import json
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class DataProviderInterface(ABC):

    def __init__(self):
        """        Initialize the object with None as the initial data.

        This method initializes the object with None as the initial data.

        Args:
            self: The object instance.
        """

        self.data = None

    @abstractmethod
    def collect_data(self):
        """        Collects data from a source and performs necessary operations.

        This method is responsible for collecting data from a specified source and performing any required operations on the data.
        """

        pass

    @abstractmethod
    def get_value(self, key):
        """        Get the value associated with the given key.

        Args:
            key (str): The key for which the value needs to be retrieved.

        Returns:
            object: The value associated with the given key.

        Raises:
            KeyError: If the key is not present in the data structure.
        """

        pass

class XMLDataProvider(DataProviderInterface):

    def __init__(self):
        """        Initializes the object with a None value for the data attribute.

        This method initializes the object with a None value for the data attribute.

        Args:
            self: The object instance.
        """

        self.data = None

    def collect_data(self):
        """        Collects data from the 'data.xml' file and stores it in the 'self.data' attribute.

        Reads the content of the 'data.xml' file using UTF-8 encoding and then parses it using BeautifulSoup with XML parser.

        Args:
            self: The instance of the class.


        Raises:
            FileNotFoundError: If the 'data.xml' file is not found.
        """

        with open("data.xml", encoding="utf-8") as file:
            data = file.read()
        bs_xml = BeautifulSoup(data, "xml")
        self.data = bs_xml
    
    def get_value(self, key):
        """        Get the value associated with the given key from the data.

        Args:
            key (str): The key to search for in the data.

        Returns:
            str or None: The value associated with the given key, or None if the key is not found.
        """

        value = self.data.find(key)
        return value.text if value else value


class Weather():
    def __init__(self, data_provider: XMLDataProvider):
        """        Initialize the class with a data provider.

        Args:
            data_provider (XMLDataProvider): An instance of XMLDataProvider used to provide data.
        """

        self.data_provider = data_provider
    
    def print_weather(self):
        """        Print the current weather information.

        This function retrieves the time, temperature, and unit of measurement from the data provider and prints a formatted string
        containing this information.

        Args:
            self (obj): The current instance of the class.
        """

        res = f"At {self.data_provider.get_value('time')} temperature is {self.data_provider.get_value('temp')} {self.data_provider.get_value('unit')}"
        print(res)

def client_code():
    """    Client code to collect and print weather data from XML data provider.

    This function initializes an XMLDataProvider object to collect data and then uses the collected data to initialize a Weather object. Finally, it prints the weather information.
    """

    xml_data_provider = XMLDataProvider()
    xml_data_provider.collect_data()
    weather = Weather(data_provider=xml_data_provider)
    weather.print_weather()

if __name__=='__main__':
    client_code()
