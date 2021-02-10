"""Tar Heels exercise redux as a structured program."""

__author__ = "730318766"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(arithmetic: int))


def tar_heels(arithmetic: int) -> str:
    """Converts booleans into corresponding TarHeel statement."""
    arithmetic: int = int(input("Enter an interger: "))
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
