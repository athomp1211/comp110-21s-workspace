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


# Example usage of the sum_algo function
odds: list[int] = [1, 3, 5, 7]
odds_sum: int = sum_algo(odds)
print(odds_sum)


single: list[int] = [110]
many: list[int] = [1, 3, 5]
print(sum_algo(single))
print(sum_algo(many))
