"""Coinflip Guessing Game."""

from random import randint

__author__ = "730318766"


PENSIVE_FACE: str = "\U0001F614"
THUMBS_UP: str = "\U0001F44D"
player: str = ""
points: int = 0
what_next: str = ""


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    global points
    greet()
    what_next: str = str(input("*Coin Flip* Heads, Tails, or End Game? (h/t/e) "))
    if what_next == "e":
        print(f"So sad to see you go {PENSIVE_FACE} You accumulated {points} points! Goodbye.")
    else:
        if what_next == "h":
            points = option_1(points)
        else:
            if what_next == "t":
                option_2()


def greet() -> None:
    """Prints a welcome message for context and asks for player's name."""
    global player
    player = str(input("What's your name? "))
    print(f"Welcome {player}, this game flips a coin & you guess heads or tails. How many can you guess correctly?")


def coin_flip() -> str:
    """Returns heads or tails from random coin flip."""
    coin: int = int(randint(1, 2))
    if coin == 1:
        return "h"
    else:
        return "t"


def option_1(points: int) -> int:
    """Returns points from Heads option."""
    if what_next == coin_flip:
        print(f"Correct {player} , here's 1 point!")
        points += 1
        total: str = str(input("Would you like to see your total points? (y/n) "))
        if total == "y":
            print(f"You currently have {points} point(s).")
        option_3()
    else:
        if what_next != coin_flip:
            print(f"Sorry, that is incorrect {player} {PENSIVE_FACE}")
            total: str = str(input("Would you like to see your total points? (y/n) "))
            if total == "y":
                print(f"You currently have {points} point(s).")
            option_3()
    return points


def option_2() -> None:
    """Reassigns points from Tails option."""
    global points
    if what_next == coin_flip:
        print(f"Correct {player} , here's 1 point!")
        points += 1
        total: str = str(input("Would you like to see your total points? (y/n) "))
        if total == "y":
            print(f"You currently have {points} points.")
        option_3()
    else:
        if what_next != coin_flip:
            print(f"Sorry, that is incorrect {player} {PENSIVE_FACE}")
            total: str = str(input("Would you like to see your total points? (y/n) "))
            if total == "y":
                print(f"You currently have {points} points.")
            option_3()


def option_3() -> None:
    """Starts game over or ends game."""
    global points
    next_step: str = str(input("Would you like to Try Again or End Game? (t/e) "))
    if next_step == "t":
        print("Congrats, here's an extra point to start you off!")
        points += 1
        main()
    else:
        if next_step == "e":
            print(f"So sad to see you go {PENSIVE_FACE} You accumulated {points} points! Goodbye.")

            
if __name__ == "__main__":
    main()