"""An exercise in remainders and boolean logic."""

__author__ = "730318766"


# Begin your solution here...
arithmetic: int = int(input("Enter an interger: "))

if arithmetic % 2 == 0 and arithmetic % 7 == 0:
    print("TAR HEELS")
else:
    if arithmetic % 2 == 0:
        print("TAR")
    else:
        if arithmetic % 7 == 0:
            print("HEELS")
        else:
            if arithmetic % 2 != 0 and arithmetic % 7 != 0:
                print("CAROLINA")