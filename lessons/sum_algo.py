"""Examples of List and Loop algorithm."""

def sum_algo(x: list[int]) -> int:
    """Summation if input list is returned."""
    # 1. Start with total and index 0
    total: int = 0
    i: int = 0
    # 2. While index is valid, i < len(x)
    while i < len(x):
        #   True- take x[i] and add to total
        total += x[i]
        #   True- increase i by 1, moving it to the next index
        i += 1
    #   False- Result is stored in total variable
    return total