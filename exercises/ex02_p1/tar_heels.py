"""Tar Heels exercise redux as a structured program."""

__author__ = "730318766"


from typing import NoReturn


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))
    NoReturn


def tar_heels(arithmetic: int) -> str:
    """Converts booleans into corresponding TarHeel statement."""
    if arithmetic % 2 == 0 and arithmetic % 7 == 0:
        return ("TAR HEELS")
    else:
        if arithmetic % 2 == 0:
            return ("TAR")
        else:
            if arithmetic % 7 == 0:
                return ("HEELS")
            else:
                if arithmetic % 2 != 0 and arithmetic % 7 != 0:
                    return ("CAROLINA")


if __name__ == "__main__":
    main()
