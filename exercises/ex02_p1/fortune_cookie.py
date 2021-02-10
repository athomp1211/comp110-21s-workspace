"""Fortune cookie exercise redux as a structured program."""

from random import randint
from typing import NoReturn

__author__ = "730318766"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Returns random fortune."""
    rand_fortune: int = int(randint(1, 4))
    if rand_fortune == 1:
        return ("A truly rich life contains love and art in abundance.")
    else:
        if rand_fortune == 2:
            return ("One can never fill another’s shoes, rather he must outgrow the old shoes.")
        else:
            if rand_fortune == 3:
                return ("Soon life will become more interesting.")
            else:
                if rand_fortune == 4:
                    return ("Your love life will be happy and harmonious.")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
