import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list[int]:
    """
    Generates a unique, sorted list of lottery numbers within a specified range, 
    printing an error message for invalid input.
    """
    
    # 1.1 Check range constraints: 1 <= min <= max <= 1000
    if not (1 <= min_value <= max_value <= 1000):
        print("Error: The minimum (>=1) and maximum (<=1000) values are outside the required range or min > max.")
        return []

    # 1.2 Check quantity constraint: Must be positive and not exceed the range size
    # Calculate range size: max_value - min_value + 1
    if not (0 < quantity <= (max_value - min_value + 1)):
        print(f"Error: The requested quantity ({quantity}) is invalid or exceeds the possible range size ({max_value - min_value + 1}).")
        return []

    numbers_in_range = list(range(min_value, max_value + 1))  # create list in specified range
    lottery_numbers = random.sample(numbers_in_range, quantity) # select required amount of unique lottery numbers 
    return sorted(lottery_numbers) # return sorted list of winning numbers


print(get_numbers_ticket(1, 36, 4))
# Example output: [5, 12, 28, 35] (The numbers will vary)

# Example of an error output:
print(get_numbers_ticket(1, 5, 10))