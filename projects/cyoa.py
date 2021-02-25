"""Coinflip Guessing Game"""

from random import randint

__author__ = "730318766"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    greet()
    player
    points: int = 0
    option_1(coin_flip(), points)
    option_3(points)


def greet() -> None:
    """Prints a welcome message for context and asks for player's name."""
    global player
    player = str(input("What's your name? "))
    print(f"Welcome {player}, to Heads or Tails! This game flips a coin, you choose whether it was heads or tails, and hope your luck is up! How many can you guess correctly in a row?")


def coin_flip() -> str:
    """Returns heads or tails from random coin flip."""
    coin: int = int(randint(1, 2))
    if coin == 1:
        return "Heads"
    else:
        if coin == 2:
            return "Tails"


def option_1(coin_flip: str, points: int) -> None:
    """Prints a goodbye message if player ends game or branches to other options."""
    what_next: str = str(input("Start Game or End Game? "))
    if what_next == "End Game":
        print(f"So sad to see you go :( You accumulated {points} points! Goodbye.")
    else:
        if what_next == "Start Game":
            option_2(coin_flip, points)
        else:
            print("Try typing your answer again and make sure to capitalize!")
            option_1(coin_flip, points)


def option_2(coin_flip: str, points: int) -> None:
    """Returns points from Heads or Tails option."""
    heads_tails: str = str(input("*Coin flip* Heads or Tails? "))
    if heads_tails == coin_flip:
        print(f"Correct {player}, here's 1 point!")
        points += 1
    else:
        if heads_tails != coin_flip:
            print(f"Sorry, that is incorrect {player} :(")


def option_3(points: int) -> int:
    """."""
    next_step: str = str(input("Would you like to Try Again or End Game? "))
    if next_step == "Try Again":
        

            
if __name__ == "__main__":
    main()