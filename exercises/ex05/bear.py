"""File to define Bear class."""


class Bear:
    """Initializing the Bear class to represent the bears in the river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing the age and hunger scores of the bears in the river."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increases the bear's age by one and decreases it's hunger score by one."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increases the bear's hunger score by the number of fish in the river."""
        self.hunger_score += num_fish
        return None
