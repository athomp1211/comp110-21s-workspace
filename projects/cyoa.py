"""Coinflip Guessing Game"""

__author__ = "730318766"


def main() -> None:
     """The entrypoint of the program, when run as a module."""
     greet()
     points: int = 


def greet() -> None:
    """Prints a welcome message for context and asks for player's name"""
    print("Welcome to Heads or Tails! This game flips a coin, you choose heads or tails, and hope your luck is up! How many can you guess correctly in a row?")
    player: str = str(input("What's your name? "))



if __name__ == "__main__":
    main()