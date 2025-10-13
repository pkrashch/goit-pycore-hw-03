from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    upcoming_birthdays = [] # Empty list for results
    
    today = datetime.today().date()
    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = user_birthday.replace(year=today.year) 
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1) # birthday this year has alredy happened
        
        days_difference = (birthday_this_year - today).days
        if 0 <= days_difference <= 6:
            congrat_date = birthday_this_year
            if congrat_date.weekday() == 5: 
                congrat_date = congrat_date + timedelta(days=2) #if Saturday, move congratulations date to the next Monday
            elif congrat_date.weekday() == 6: 
                congrat_date = congrat_date + timedelta(days=1) #if Sunday, move congratulations date to the next Monday
            congrat_date_str = congrat_date.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congrat_date_str })
            
    return upcoming_birthdays #return upcoming list of birthdays
    

users = [
    {"name": "John Doe", "birthday": "1985.10.13"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)