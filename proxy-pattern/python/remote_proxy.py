from abc import ABC, abstractmethod

class RemoteObject(ABC):
    @abstractmethod
    def perform_action(self):
        """        Perform the action.

        This method performs the action specified for the object.
        """

        pass

class RealRemoteObject(RemoteObject):
    def perform_action(self):
        """        Print a message indicating that the RealRemoteObject is performing an action.

        This method prints a message to indicate that the RealRemoteObject is performing an action.
        """

        print("RealRemoteObject performing action")

class RemoteProxy(RemoteObject):
    def __init__(self):
        """        Initialize the object with a None value for the _real_object attribute.

        This method initializes the object with a None value for the _real_object attribute.

        Args:
            self: The object itself.
        """

        self._real_object = None

    def perform_action(self):
        """        Perform an action using the real remote object.

        If the real remote object is not initialized, it creates a new instance of RealRemoteObject and then performs the action using it.
        """

        if self._real_object is None:
            self._real_object = RealRemoteObject()
        self._real_object.perform_action()

# Client code
proxy = RemoteProxy()
proxy.perform_action()