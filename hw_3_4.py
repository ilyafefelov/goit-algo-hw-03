from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    Returns a list of upcoming birthdays within the next 7 days.

    Args:
        users (list): A list of dictionaries representing user information. Each dictionary should have a "name" and "birthday" key.

    Returns:
        list: A list of dictionaries containing the name of the user and the date of the upcoming birthday in the format "%Y.%m.%d".
    """
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()
        
        if birthday_this_year < today:
            birthday_this_year = datetime(today.year + 1, birthday.month, birthday.day).date()
        
        days_before_birthday = (birthday_this_year - today).days
        
        if days_before_birthday <= 7:
            if birthday_this_year.weekday() >= 5:  # If birthday falls on a weekend
                days_before_birthday += 7 - birthday_this_year.weekday()  # Move to next Monday
            
            congratulation_date = today + timedelta(days=days_before_birthday)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    
    return upcoming_birthdays

users = [
    {"name": "Loid Poss", "birthday": "1985.01.23"},
    {"name": "Anna Smith", "birthday": "1990.01.27"},
    {"name": "Mark Test", "birthday": "1990.04.24"},
    {"name": "Karl Test2", "birthday": "1992.04.21"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
# map upcoming_birthdays to a list of names
upcoming_birthdays = list(map(lambda x: x["name"], upcoming_birthdays))

# Tests
print("The list of birthdays this week: ", upcoming_birthdays)
