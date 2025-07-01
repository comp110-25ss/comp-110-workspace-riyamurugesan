"""Challenge Question: Functions"""

__author__ = "730766142"


def mimic(message: str) -> str:
    """Returns a message back to you!"""
    return message


def main() -> None:
    """Prints the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
