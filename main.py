from datetime import datetime

def get_days_from_today(date_str: str) -> int:
    """
    Return the number of days from the given date (format 'YYYY-MM-DD') to today.
    Positive for past dates, negative for future dates.

    Raises:
        ValueError: if the input is not a valid 'YYYY-MM-DD' date.
    """
    try:
        entered_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as e:
        # error handling
        raise ValueError("Invalid date. Please use format YYYY-MM-DD, e.g., 2020-10-09.") from e
     
    current_date = datetime.today().date() #date only     
    return (current_date - entered_date).days

while True:
        s = input("Please enter the date (YYYY-MM-DD): ").strip()
        try:
            days = get_days_from_today(s)
            print(days)
            break  # exit after valid input
        except ValueError as err:
            print(err)