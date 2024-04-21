import random


def get_numbers_ticket(min, max, quantity):
    """
    Generate a list of unique random numbers within a given range.

    Args:
        min (int): The minimum value of the range (inclusive).
        max (int): The maximum value of the range (inclusive).
        quantity (int): The number of random numbers to generate.

    Returns:
        list: A sorted list of unique random numbers within the given range.

    Raises:
        None

    """
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return []
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    
    return sorted(list(numbers))

print(get_numbers_ticket(2, 999, 4))