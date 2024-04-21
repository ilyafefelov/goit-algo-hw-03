import datetime


def get_days_from_today(date):
    """
    Calculates the number of days between the current date and the input date.

    Args:
        date (str): The input date in the format 'YYYY-MM-DD'.

    Returns:
        int: The number of days between the current date and the input date.

    Raises:
        ValueError: If the input date is in the wrong format.

    """
    try:
        # Convert the input date string to a datetime object
        input_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        
        # Get the current date
        current_date = datetime.datetime.today()
        
        # Calculate the difference in days between the current date and the input date
        days_difference = (current_date - input_date).days
        
        return days_difference
    except ValueError:
        # Handle the case when the input date is in the wrong format
        print("Invalid date format. Please provide the date in the format 'YYYY-MM-DD'")
        return None

# Test the function with a valid date
print(get_days_from_today('2020-10-01')) 
print(get_days_from_today('2022-07-30')) 