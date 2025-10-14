from datetime import datetime

def get_days_from_today(date_str: str) -> int | None:
    """
    Return the number of days from the given date (format 'YYYY-MM-DD') to today.
    Positive for past dates, negative for future dates.

    Raises:
        ValueError: if the input is not a valid 'YYYY-MM-DD' date.
    """
    try:
        entered_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        # error handling
        print("Invalid date. Please use format YYYY-MM-DD, e.g., 2020-10-09.")
        return None
     
    current_date = datetime.today().date() #date only     
    return (current_date - entered_date).days

dates_to_check = [
    "2023-05-15", # Коректна дата в минулому
    "2026-12-31", # Коректна дата в майбутньому
    "2024/09/01", # Некоректний формат
    "2022-02-30", # Некоректна дата (неіснуючий день)
    "2025-10-14"  # Приблизно сьогодні
]

print("--- Обробка списку дат ---")
for date_item in dates_to_check:
    result = get_days_from_today(date_item)
    
    if result is not None:
        print(f"Дата: {date_item} -> Різниця: {result} днів.")
    else:
        # Програма продовжує працювати, незважаючи на помилку
        print(f"Дата: {date_item} -> Обробка пропущена.") 