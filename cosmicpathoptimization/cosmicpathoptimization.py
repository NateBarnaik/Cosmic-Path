import sys
import statistics
from typing import List


def answer(temps: List[int]) -> int:
    """Finds and prints the mean from a list of integers, as a integer

    Args:
        temps (List[int]): List of temps

    Returns:
        int: Mean of the list of temps, printed as an int
    """
    return int(statistics.mean(temps))


def main() -> None:
    """Main function
    """
    x = int(sys.stdin.readline())
    temps = [int(y) for y in sys.stdin.readline().split(' ', x)]
    print(answer(temps))


if __name__ == "__main__":
    main()
