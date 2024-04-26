import json
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class DataProviderInterface(ABC):

    def __init__(self):
        """        Initialize the object with a None value for data.

        This method initializes the object with a None value for the data attribute.

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
            KeyError: If the key is not present in the dictionary.
        """

        pass

class XMLDataProvider(DataProviderInterface):

    def __init__(self):
        """        Initializes the object with a None value for data.

        This method initializes the object with a None value for the data attribute.

        Args:
            self: The object instance.
        """

        self.data = None

    def collect_data(self):
        """        Collects data from an XML file and stores it in the 'data' attribute.

        Reads the content of the 'data.xml' file using UTF-8 encoding and parses it using BeautifulSoup.

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
            str or None: The value associated with the key, or None if the key is not found.
        """

        value = self.data.find(key)
        return value.text if value else value

class JSONDataProviderInterface(ABC):

    @abstractmethod
    def read_json_data(self):
        """        Reads and returns the JSON data from a source.

        Returns:
            dict: A dictionary containing the JSON data.
        """

        pass

    @abstractmethod
    def get_value_from_json(self):
        """        Get value from a JSON object.

        This method retrieves a value from a JSON object using the provided key.

        Returns:
            Any: The value associated with the provided key in the JSON object.
        """

        pass

class JSONDataProvider(JSONDataProviderInterface):

    def __init__(self):
        """        Initialize the object with a None value for the data attribute.

        This method initializes the object with a None value for the data attribute.

        Args:
            self: The object instance.
        """

        self.data = None

    def read_json_data(self):
        """        Read data from a JSON file and store it in the 'data' attribute.

        Reads the data from the 'data.json' file using UTF-8 encoding and stores it in the 'data' attribute of the object.

        Args:
            self: The object instance.


        Raises:
            FileNotFoundError: If the 'data.json' file is not found.
            JSONDecodeError: If the data in the file is not valid JSON.
        """

        with open("data.json", encoding="utf-8") as file:
            data = json.load(file)
        self.data = data
    
    def get_value_from_json(self, key):
        """        Get the value associated with the given key from the JSON data.

        Args:
            key (str): The key for which the value needs to be retrieved from the JSON data.

        Returns:
            Any: The value associated with the given key from the JSON data, or None if the key is not present.
        """

        return self.data.get(key)

class JSONtoXMLAdapter(DataProviderInterface):

    def __init__(self, json_provider: JSONDataProvider):
        """        Initialize the class with a JSON data provider.

        Args:
            json_provider (JSONDataProvider): An instance of JSONDataProvider used to provide JSON data.
        """

        self.json_provider = json_provider
    
    def collect_data(self):
        """        Collects data by reading JSON data using the json_provider.

        This method collects data by reading JSON data using the json_provider.
        """

        self.json_provider.read_json_data()
    
    def get_value(self, key):
        """        Get the value associated with the given key from the JSON provider.

        Args:
            key (str): The key for which the value needs to be retrieved.

        Returns:
            Any: The value associated with the given key from the JSON provider.
        """

        return self.json_provider.get_value_from_json(key)


class Weather():
    def __init__(self, data_provider: XMLDataProvider):
        """        Initialize the class with a data provider.

        Args:
            data_provider (XMLDataProvider): An XML data provider object.
        """

        self.data_provider = data_provider
        self.data_provider.collect_data()
    
    def print_weather(self):
        """        Print the current weather information.

        This function retrieves the time, temperature, and unit from the data provider and prints a formatted string
        containing this information.
        """

        res = f"At {self.data_provider.get_value('time')} temperature is {self.data_provider.get_value('temp')} {self.data_provider.get_value('unit')}"
        print(res)

# def client_code():
#     xml_data_provider = XMLDataProvider()
#     weather = Weather(data_provider=xml_data_provider)
#     weather.print_weather()

def client_code():
    """    Client code to demonstrate the use of JSONDataProvider, JSONtoXMLAdapter, and Weather classes.

    This function creates an instance of JSONDataProvider, adapts it to XMLDataProvider using JSONtoXMLAdapter,
    and then uses the Weather class to print the weather information.
    """

    json_provider = JSONDataProvider()
    xml_json_adapter = JSONtoXMLAdapter(json_provider)
    weather = Weather(data_provider=xml_json_adapter)
    weather.print_weather()

if __name__=='__main__':
    client_code()
