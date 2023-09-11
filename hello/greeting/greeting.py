"""Greeting library
"""

def generate(to_whom: str, greeting: str) -> str: 
    """Provides a greeting

    Args:
        to_whom (str): The person to whom the greeting should be directed
        greeting (str): The salutation, e.g. 'Hello', 'Goodbye', etc.
    """
    return f"Hello {to_whom}, {greeting}"