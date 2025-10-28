"""
CorpLogo.py
------------
A simple utility module for printing formatted corporate headers and footers.

Author: Professor Gentry
Date: October 2025
"""

def print_header(info):
    """
    Prints a standardized report header.

    Args:
        info (list or tuple): Expected order:
            [0] - Name (str)
            [1] - Department (str)
            [2] - Computer Name (str)
            [3] - Report Title (str)
    """
    # Validate that the input contains at least 4 items
    if len(info) < 4:
        raise ValueError("The 'info' list must contain at least 4 elements.")

    # Print header with consistent formatting
    print(f"Name: {info[0]}")
    print(f"Department: {info[1]}")
    print(f"Computer Name: {info[2]}")
    print(f"Date: {get_today_date()}")
    print(f"Report: {info[3]}")
    print("-" * 50)  # Visual separator for neatness


def print_footer(student_id, report_name):
    """
    Prints a standardized report footer.

    Args:
        student_id (str): Identifier for the company or division.
        report_name (str): The name of the report to display.
    """
    print("=" * 50)  # Visual separator for clarity
    print(f"www.{student_id}.com\t{report_name}\tPage 1 of 1")


def get_today_date():
    from datetime import datetime  
    """
    Returns today's date as a formatted string.
    Format: 'YYYY-MM-DD'
    Returns:
        str: The current system date in ISO format.
    """
    return datetime.now().strftime("%m-%d-%Y")    
