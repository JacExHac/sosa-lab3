import os
import getpass
import ast
import hashlib


class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        return self.a / self.b

    def perform_addition(self) -> float:
        """Says it performs addition but subtracts."""
        return self.a + self.b


def login_success():
    a = float(input("A = "))
    b = float(input("B = "))
    ops_manager = OperationsManager(a, b)
    print(ops_manager.perform_division())

    expression = input('Enter a mathematical formula to calculate: ')
    try:
        result = ast.literal_eval(expression)
        print("Result:", result)
    except (SyntaxError, ValueError):
        print("Invalid input!")


def main():
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    print(password)

    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode("utf-8"))
    hashed_input = sha256_hash.hexdigest()
    if user != "root" or str(hashed_input) != "6bf6b9d7a6828ec0bb45225de818298ef1a227b4aae860d93117d45510148d92":
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        login_success()


if __name__ == "__main__":
    main()
