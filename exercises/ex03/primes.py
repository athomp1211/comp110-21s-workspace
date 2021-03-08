"""EX03 - prime functions."""

__author__: str = "730318766"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(3))
    print(is_prime(6))
    print(is_prime(31))
    print(is_prime(110))
    print(list_primes(3, 7))
    print(list_primes(10, 20))
    print(list_primes(25, 28))
    print(list_primes(-1, 5))


def is_prime(x: int) -> bool:
    """Returns true or false for argument being prime or not."""
    i: int = abs(x) - 1
    if i == 0 or x == 0:
        i -= 1
        return False
    while i > 1:
        if abs(x) % i != 0:
            i -= 1
        else:
            if abs(x) % i == 0:
                return False
    return True


def list_primes(a: int, b: int) -> list[int]:
    """Returns a list of all prime numbers between 1st(inclusive) and 2nd(exclusive) int arguments."""
    prime_nums: list[int] = []
    non_primes: list[int] = []
    nums: range = range(a, b)
    i: int = 0
    while i < len(nums):
        if is_prime(nums[i]) is True:
            prime_nums.append(nums[i])
            i += 1
        else:
            if is_prime(nums[i]) is False:
                non_primes.append(nums[i])
                i += 1
    return prime_nums


if __name__ == "__main__":
    main()