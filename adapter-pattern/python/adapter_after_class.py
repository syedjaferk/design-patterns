"""
Adapter class with class based implementation
"""
import json
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class DataProviderInterface(ABC):
    """
    DataProvider Interface
    Methods:
        collect_data: to collect the data
        get_value: to get the value from data
    """

    def __init__(self):
        """        Initializes the object with a None value for the data attribute.

        This method initializes the object by setting the data attribute to None.

        Args:
            self: The object instance.
        """

        self.data = None

    @abstractmethod
    def collect_data(self):
        """        Method to collect the data.

        This method collects the data required for further processing.
        """
        pass

    @abstractmethod
    def get_value(self, key):
        """        Method to get value from data.

        Args:
            key (str): The key to retrieve the value from the data.

        Returns:
            Any: The value associated with the given key in the data.
        """
        pass


class XMLDataProvider(DataProviderInterface):
    """
    DataProvider: XML Data Provider
    """
    def __init__(self):
        """        Initialization of the attr.

        This method initializes the 'data' attribute to None.

        Args:
            self: The object instance.
        """
        self.data = None

    def collect_data(self):
        """        Collects and parses data from an XML file.

        Reads the data from the specified XML file and parses it using BeautifulSoup.

        Args:
            self: The object instance.
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

class JSONDataProviderInterface(ABC):

    @abstractmethod
    def read_json_data(self):
        """        Reads and returns JSON data from a file.

        This function reads JSON data from a file and returns it as a Python object.

        Returns:
            dict: A Python dictionary representing the JSON data.
        """

        pass

    @abstractmethod
    def get_value_from_json(self):
        """        Get the value from a JSON object.

        This method retrieves a value from a JSON object using the specified key.

        Returns:
            Any: The value associated with the specified key in the JSON object.
        """

        pass

class JSONDataProvider(JSONDataProviderInterface):

    def __init__(self):
        """        Initialize the object with a None value for data.

        This method initializes the object with a None value for the data attribute.

        Args:
            self: The object instance.
        """

        self.data = None

    def read_json_data(self):
        """        Read and load JSON data from a file.

        This function reads and loads JSON data from a file named "data.json" using UTF-8 encoding.

        Args:
            self: The instance of the class.


        Raises:
            FileNotFoundError: If the file "data.json" does not exist.
            JSONDecodeError: If the content of the file is not valid JSON.
        """

        with open("data.json", encoding="utf-8") as file:
            data = json.load(file)
        self.data = data
    
    def get_value_from_json(self, key):
        """        Get the value associated with the given key from the JSON data.

        Args:
            key (str): The key for which the value needs to be retrieved.

        Returns:
            The value associated with the given key from the JSON data.
        """

        return self.data.get(key)

class JSONtoXMLAdapter(JSONDataProvider, XMLDataProvider):
    
    def collect_data(self):
        """        Collects data from the JSON data provider.

        This method initializes a JSONDataProvider object and reads JSON data using it.
        """

        self.json_data_provider = JSONDataProvider()
        self.json_data_provider.read_json_data() 
    
    def get_value(self, key):
        """        Get the value associated with the given key from the JSON data provider.

        Args:
            key (str): The key for which the value needs to be retrieved.

        Returns:
            Any: The value associated with the given key from the JSON data provider.
        """

        return self.json_data_provider.get_value_from_json(key)


class Weather():
    def __init__(self, data_provider: XMLDataProvider):
        """        Initialize the class with a data provider.

        Args:
            data_provider (XMLDataProvider): An instance of XMLDataProvider used to collect data.
        """

        self.data_provider = data_provider
        self.data_provider.collect_data()
    
    def print_weather(self):
        """        Print the current weather information.

        This function retrieves the current time, temperature, and unit from the data provider and prints a formatted string
        containing this information.
        """

        res = f"At {self.data_provider.get_value('time')} temperature is {self.data_provider.get_value('temp')} {self.data_provider.get_value('unit')}"
        print(res)

# def client_code():
#     xml_data_provider = XMLDataProvider()
#     weather = Weather(data_provider=xml_data_provider)
#     weather.print_weather()

def client_code():
    """    Client code to print weather information using JSONtoXMLAdapter.

    This function creates an instance of JSONtoXMLAdapter to adapt JSON data to XML format
    and then uses it to create an instance of Weather to print weather information.
    """

    xml_json_adapter = JSONtoXMLAdapter()
    weather = Weather(data_provider=xml_json_adapter)
    weather.print_weather()

if __name__=='__main__':
    client_code()
