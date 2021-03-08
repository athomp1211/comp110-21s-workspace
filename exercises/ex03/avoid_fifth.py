"""EX03 - avoid_fifth function."""

__author__: str = "730318766"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("Hello :)"))
    print(avoid_fifth("Early to bed and early to rise makes a man healthy, wealthy and wise."))


def avoid_fifth(x: str) -> str:
    """Loops through given str and returns output without e's in it"""
    y: str = ""
    i: int = 0
    while i < len(x):
        if x[i] == "e":
            i += 1
        else:
            if x[i] == "E":
                i += 1
            else:
                 y += x[i]
                 i += 1
    return y


if __name__ == "__main__":
    main()