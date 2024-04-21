import re


def normalize_phone(phone_number):
    """
    Normalize a phone number by removing non-digit characters and adding an international code if missing.

    Args:
        phone_number (str): The phone number to be normalized.

    Returns:
        str: The normalized phone number.

    Example:
        >>> normalize_phone('+(067) 456-7890')
        '+380674567890'
    """
    phone_number = re.sub(r'\D', '', phone_number)
    
    if not phone_number.startswith('+'):
        phone_number = '+38' + phone_number
    
    return phone_number

# Tests
print(normalize_phone('+(067) 456-7890'))  # '+380674567890'    
print(normalize_phone('067-456-9090'))  # '+380674569090'