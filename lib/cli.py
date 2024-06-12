# lib/cli.py

from manager import Manager


def get_manager():
    print("The Artists assigned to a manager with their various Songs and Genre")
    a = input ("Enter Manager's name: ")
    b = input ("Enter Song Genre: ")

    manager = Manager(a, b)
    print(manager)

# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. Some useful function")


if __name__ == "__main__":
       get_manager
