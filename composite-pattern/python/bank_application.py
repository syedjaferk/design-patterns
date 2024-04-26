from abc import ABC, abstractmethod

# Component
class AccountComponent(ABC):
    @abstractmethod
    def get_balance(self):
        """        Get the current balance of the account.

        Returns:
            float: The current balance of the account.
        """

        pass

    @abstractmethod
    def get_statement(self):
        """        Get the statement associated with the current object.

        Returns:
            str: The statement associated with the current object.
        """

        pass

# Leaf
class BankAccount(AccountComponent):
    def __init__(self, account_number, balance, statement):
        """        Initialize an instance of the Account class.

        Args:
            account_number (int): The account number for the account.
            balance (float): The initial balance for the account.
            statement (str): The statement associated with the account.
        """

        self.account_number = account_number
        self.balance = balance
        self.statement = statement

    def get_balance(self):
        """        Returns the current balance of the account.

        Returns:
            float: The current balance of the account.
        """

        return self.balance

    def get_statement(self):
        """        Returns the account statement for the current account.

        Returns:
            str: The account statement for the current account.
        """

        return f"Account {self.account_number} Statement:\n{self.statement}"

# Composite
class CustomerAccount(AccountComponent):
    def __init__(self, customer_name):
        """        Initialize a new customer with the given name.

        Args:
            customer_name (str): The name of the customer.
        """

        self.customer_name = customer_name
        self.accounts = []

    def add_account(self, account):
        """        Add an account to the list of accounts.

        Args:
            account: The account to be added.
        """

        self.accounts.append(account)

    def get_balance(self):
        """        Get the total balance of all accounts in the portfolio.

        This function calculates the total balance by summing the individual balances of all accounts in the portfolio.

        Returns:
            float: The total balance of all accounts in the portfolio.
        """

        total_balance = sum(account.get_balance() for account in self.accounts)
        return total_balance

    def get_statement(self):
        """        Returns a consolidated statement for the customer.

        This function generates a consolidated statement for the customer by iterating through each account
        and appending its statement to the consolidated statement.

        Returns:
            str: The consolidated statement for the customer.
        """

        consolidated_statement = f"Consolidated Statement for {self.customer_name}:\n"
        for account in self.accounts:
            consolidated_statement += account.get_statement() + "\n"
        return consolidated_statement

# Usage
if __name__ == "__main__":
    account1 = BankAccount("123456", 5000, "Transaction 1: +$100\nTransaction 2: -$50")
    account2 = BankAccount("789012", 7000, "Transaction 1: +$200\nTransaction 2: -$100")

    customer = CustomerAccount("John Doe")
    customer.add_account(account1)
    customer.add_account(account2)

    # Generate Customer’s total account balance
    total_balance = customer.get_balance()
    print(f"Customer's Total Account Balance: ${total_balance}")

    # Generate Consolidated account statement
    consolidated_statement = customer.get_statement()
    print(consolidated_statement)
