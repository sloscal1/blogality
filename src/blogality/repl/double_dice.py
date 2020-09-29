""" Monte Carlo simulation of Causality 1.6 (pg 3)

A simple example of rolling two dice and seeing how
often they come up with the same number. The experiment
is repeated a few times, counting over different numbers
of tosses.

"""
from blogality.objects.dice import Die


def count_matching(d1: Die, d2: Die, num_rolls: int) -> int:
    """ Roll the given dice a number of times and count when they match.

    Args:
        d1 (Die): One Die object (must not be None)
        d2 (Die): Another Die object (must not be None)
        num_rolls (int): Positive number of rolls to toss.

    Returns:
        int number of times both dice showed the same number.

    """
    matching = 0
    for _ in range(num_rolls):
        matching += int(d1.roll() == d2.roll())
    return matching


def main():
    print("Going to get two dice, roll them a bunch of times and see how many doubles we get!")
    d1 = Die(randseed=42)
    d2 = Die(randseed=1337)
    print("Verifying that the two dice give different results...")
    rolls = [d1.roll() for _ in range(10)]
    print(f"Die 1: {rolls}")
    rolls = [d2.roll() for _ in range(10)]
    print(f"Die 2: {rolls}")

    max_rolls = [10, 100, 1_000, 10_000, 100_000, 1_000_000]
    for num_rolls in max_rolls:
        # Go back to the initial conditions... just to demonstrate that functionality
        # But you can imagine saying: what if we started the
        # experiment throwing dice 100 times instead of 10 times...
        d1.restart()
        d2.restart()
        matching = count_matching(d1, d2, num_rolls)
        print(f"Rolled both dice {num_rolls} times, doubles happened {matching} times ({matching/num_rolls:0.4f})")

    print(f"The expected answer is 1/6 ({1/6:0.4f})")


if __name__ == "__main__":
    main()
