"""Planning a tea party based on the number of guests!"""

__author__ = "730766142"


def main_planner(guests: int) -> None:
    """Combines all functions and produces printed output."""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # need to convert 'guests' to a string to allow program to properly concatenate
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print(
        "Cost: $" + str(cost(tea_bags(guests), treats(guests)))
    )  # dollar sign isn't included in cost function result so we must add it to string


def tea_bags(people: int) -> int:
    """Computes number of tea bags based on number of guests"""
    return 2 * people


def treats(people: int) -> int:
    """Computes number of treats based on the number of teas"""
    return int(
        1.5 * tea_bags(people=people)
    )  # had to convert to int because 1.5 would've made the product a float!


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of the tea bags and the treats combined"""
    return (0.5 * tea_count) + (0.75 * treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
