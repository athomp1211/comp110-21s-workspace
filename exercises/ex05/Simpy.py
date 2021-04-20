"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730318766"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize the values attribute of a newly constructed Simpy object."""
        self.values = values

    def __repr__(self) -> str:
        """Magic method to represent object as string."""
        return f"Simpy({self.values})" 

    def fill(self, water: float, ounces: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        self.values = []
        for i in range(ounces):
            self.values.append(water)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the values attribute with range of values in terms of floats."""
        self.values = []
        assert step != 0.0
        while abs(start) < abs(stop):
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Returns the sum of all items in the values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds the ability to use the addition operator in conjunction with Simpy objects and floats."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return Simpy(result)

    def __pow__(self, power: Union[float, Simpy]) -> Simpy:
        """Adds the ability to use the power operator in conjunction with Simpy objects and floats."""
        result: list[float] = []
        if isinstance(power, float):
            for item in self.values:
                result.append(item ** power)
        else:
            assert len(self.values) == len(power.values)
            for i in range(len(self.values)):
                result.append(self.values[i] ** power.values[i])
        return Simpy(result)

    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds the ability to use the modulus/remainder operator in conjunction with Simpy objects and floats."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item % rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] % rhs.values[i])
        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the equality of each item in the values attribute with another Simpy object or float."""
        mask: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                mask.append(item == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                mask.append(self.values[i] == rhs.values[i])
        return mask

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the greater than relationship between each item in the values attribute with another Simpy object or float."""
        mask: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                mask.append(item > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                mask.append(self.values[i] > rhs.values[i])
        return mask

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adds the ability to use the subscription operator with Simpy objects."""
        result: list[float] = []
        if isinstance(rhs, int):
            for i in range(len(self.values)):
                result.append(self.values[i])
            return result[rhs]
        else:
            assert len(self.values) == len(rhs)
            for i in range(len(self.values)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result) 