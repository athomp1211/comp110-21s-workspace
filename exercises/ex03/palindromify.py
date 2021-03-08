"""EX03 - palindromify function."""

__author__: str = "730318766"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))


def palindromify(x: str, y: bool) -> str:
    """Transforms str input into palindrome."""
    i: int = (len(x) - 1)
    if y == True:
         while i >= 0:
            x += x[i]
            i -= 1
    else:
        if y == False:
            while i > 0:
                x += x[i - 1]
                i -= 1
    return x


if __name__ == "__main__":
    main()