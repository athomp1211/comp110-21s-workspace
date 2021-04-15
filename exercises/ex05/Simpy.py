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

    def fill()