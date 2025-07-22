"""File to define Fish class."""


class Fish:
    """Initializing the Fish class to represent the fish in the river."""

    age: int

    def __init__(self):
        """Initializing the age of the fish in the river."""
        self.age = 0
        return None

    def one_day(self):
        """Increases the fish's age by one."""
        self.age += 1
        return None
