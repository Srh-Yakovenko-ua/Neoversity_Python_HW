import random


def validate_lottery_parameters(min_num: int, max_num: int, quantity: int)-> None:
    """
        Validates the input parameters for the lottery number generation.

        Args:
            min_num (int): The minimum number in the lottery range.
            max_num (int): The maximum number in the lottery range.
            quantity (int): The number of unique lottery numbers to generate.

        Raises:
            TypeError: If any of the input parameters are not integers.
            ValueError: If the range is invalid or if the quantity exceeds the available range size.
        """
    if not all(isinstance(i, int) for i in [min_num, max_num, quantity]):
        raise TypeError("All input parameters must be integers.")


    available_range_size = max_num - min_num + 1
    if min_num > max_num:
        raise ValueError(f"Minimum ({min_num}) cannot be greater than maximum ({max_num}).")
    if not (1 <= min_num <= max_num <= 1000):
        raise ValueError("Invalid range. Minimum must be ≥ 1 and maximum must be ≤ 1000.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    if quantity > available_range_size:
        raise ValueError(f"Quantity exceeds the available range ({available_range_size}).")





def generate_unique_lottery_numbers(min_num: int, max_num: int, quantity: int)-> list[int]:
    return random.sample(range(min_num, max_num + 1), quantity)


def get_numbers_ticket(min_num, max_num, quantity):
    validate_lottery_parameters(min_num, max_num, quantity)

    ticket_numbers = generate_unique_lottery_numbers(min_num, max_num, quantity)

    return sorted(ticket_numbers)





if __name__ == "__main__":

    try:
        lottery_numbers = get_numbers_ticket(1, 10, 4)
        print("Your lottery numbers:", lottery_numbers)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
