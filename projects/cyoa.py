"""Coinflip Guessing Game"""

from random import randint

__author__ = "730318766"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    greet()
    points += 1
    options: int = int(input("*Coin Flip* Heads, Tails, or End Game? "))
    if options == "End Game":
        print(f"So sad to see you go {player} :( You accumulated {points}! Goodbye.")
    else:
        where_next(coin_flip())


def greet() -> None:
    """Prints a welcome message for context and asks for player's name."""
    player: str = str(input("What's your name? "))
    print(f"Welcome {player}, to Heads or Tails! This game flips a coin, you choose whether it was heads or tails, and hope your luck is up! How many can you guess correctly in a row?")


def coin_flip() -> str:
    """Returns heads or tails from random coin flip."""
    coin: int = int(randint(1, 2))
    if coin == 1:
        return "Heads"
    else:
        if coin == 2:
            return "Tails"
    
    
def where_next() -> str:
    """Returns points from option choice."""
    options
    if coin_flip == options:

    

if __name__ == "__main__":
    main()