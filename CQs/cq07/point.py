"""Creating a Point Class."""

from __future__ import annotations

__author__: str = "730766142"


class Point:
    """Creating a Point class that has both x and y attributes."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Initializing the x and y attributes of a Point."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates a Point by multiplying the x and y attributes by the factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new Point with x and y attributes that are scaled by the factor."""
        scaled_point: Point = Point(self.x * factor, self.y * factor)
        return scaled_point

    def __str__(self) -> str:
        """String representation of points!"""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: int) -> Point:
        """Creates a new Point with x and y attributes that are scaled by the factor."""
        scaled_point: Point = Point(self.x * factor, self.y * factor)
        return scaled_point

    def __add__(self, number: float) -> Point:
        """Creates a new Point that adds the given number to the x and y attributes."""
        new_point: Point = Point(self.x + number, self.y + number)
        return new_point
