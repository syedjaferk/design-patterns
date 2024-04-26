class RealObject:
    def perform_action(self):
        """        Perform the action of the RealObject.

        This method prints a message indicating that the RealObject is performing an action.
        """

        print("RealObject performing action")

class Proxy:
    def __init__(self, user):
        """        Initialize the object with a user.

        Args:
            user (str): The user for whom the object is being initialized.
        """

        self._real_object = RealObject()
        self._user = user

    def perform_action(self):
        """        Perform an action based on the user's role.

        If the user is an admin, the action is performed by the real object.
        If the user is not an admin, access is denied for non-admin user.
        """

        if self._user == "admin":
            self._real_object.perform_action()
        else:
            print("Access denied for non-admin user")

# Client code
admin_proxy = Proxy("admin")
admin_proxy.perform_action()

user_proxy = Proxy("user")
user_proxy.perform_action()