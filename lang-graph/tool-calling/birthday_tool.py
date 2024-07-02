from datetime import date, datetime
from typing import Optional, Union

from langchain_core.tools import tool

@tool
def get_birthdays() -> list[dict]:
    """
    Get all birthdays from the database.

    Returns:
        list[dict]: A list of birthday dictionaries.
    """

    print("Getting birthdays...")

    return []

@tool
def search_birthdays(
    name: Optional[str] = None,
    date: Optional[Union[str, date, datetime]] = None,
) -> list[dict]:
    """
    Search for birthdays based on name or date.

    Args:
        name (Optional[str], optional): The name of the person to search for. Defaults to None.
        date (Optional[Union[str, date, datetime]], optional): The date to search for. Defaults to None.
    
    Returns:
        list[dict]: A list of birthday dictionaries matching the search criteria.
    """

    print("Searching birthdays...")
    print(f"Name: {name}")
    print(f"Date: {date}")

    return []

@tool
def add_birthday(name: str, date: Union[str, date, datetime]) -> str:
    """
    Add a birthday to the database.

    Args:
        name (str): The name of the person to add.
        date (Union[str, date, datetime]): The date of the birthday to add.
    
    Returns:
        str: A success message.
    """

    print("Adding birthday...")
    print(f"Name: {name}")
    print(f"Date: {date}")

    return "Birthday added successfully."

@tool
def remove_birthday(name: str) -> str:
    """
    Remove a birthday from the database.

    Args:
        name (str): The name of the person whose birthday to remove.
    
    Returns:
        str: A success message.
    """

    return "Birthday removed successfully."