"""
This function takes in a password as a string, checks if it matches a predefined password,
and returns a Boolean value indicating whether the password is correct or not.
"""


def check_password(password, correct_password):
    """
    Check if the input password matches the correct password.

    Args:
        password (str): The input password.
        correct_password (str): The correct password.

    Returns:
        bool: True if the input password matches the correct password,
              False otherwise.

    Raises:
        ValueError: If the input password is empty.
    """
    if not password:
        raise ValueError("Password cannot be empty.")
    elif password == correct_password:
        return True
    else:
        return False
