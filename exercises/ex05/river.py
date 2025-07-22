"""File to define River class."""

__author__: str = "730766142"

from exercises.ex05.fish import Fish
from exercises.ex05.bear import Bear


class River:
    """Creating River class that tells the day and stores bear and fish populations."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes bears older than 5 and fish older than 3."""
        new_bears: list[Bear] = []
        new_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.bears = new_bears
        self.fish = new_fish
        return None

    def remove_fish(self, amount: int):
        """Removes fish from the beginning of the self.fish list."""
        i: int = 0
        while i < amount:
            self.fish.pop(0)
            i += 1
        return None

    def bears_eating(self):
        """Removes 3 fish from river and increases bear's hunger score accordingly."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Removes bear from river if it starves - hunger score less than 0."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears
        return None

    def repopulate_fish(self):
        """Each pair of fish produces 4 offspring."""
        if len(self.fish) % 2 == 0:
            pairs_of_fish: int = int(len(self.fish) / 2)
            i: int = 0
            while i < (pairs_of_fish * 4):
                self.fish.append(Fish())
                i += 1
        else:
            pairs_of_fish = int((len(self.fish) - 1) / 2)
            i = 0
            while i < (pairs_of_fish * 4):
                self.fish.append(Fish())
                i += 1
        return None

    def repopulate_bears(self):
        """Each pair of bears produces 1 offspring."""
        if len(self.bears) % 2 == 0:
            # separating whether there is a perfect split of bears or an odd number
            pairs_of_bears: int = int(len(self.bears) / 2)
            i: int = 0
            while i < pairs_of_bears:
                self.bears.append(Bear())
                i += 1
        else:
            pairs_of_bears = int((len(self.bears) - 1) / 2)
            i = 0
            while i < pairs_of_bears:
                self.bears.append(Bear())
                i += 1
        return None

    def view_river(self):
        """Prints the number of fish and bears in the river on a certain day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        i: int = 1
        while i < 8:
            self.one_river_day()
            i += 1
