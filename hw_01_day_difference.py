from datetime import datetime

format_date = '%Y-%m-%d'
def parse_date_from_string(date: str) -> datetime:
    """
      Function to parse a date string into a datetime object.

      Args:
          date (str): The date string in the format 'YYYY-MM-DD'.

      Returns:
          datetime: The corresponding datetime object.
      """
    return datetime.strptime(date, format_date)

def get_days_from_today(date: str) -> int:
    """
     Function to calculate the number of days between today and a given date.

     Args:
         date (str): The date string in the format 'YYYY-MM-DD'.

     Returns:
         int: The number of days difference between today and the provided date.

     Raises:
         ValueError: If the date string is empty or the format is incorrect.
     """
    if not date:
        raise ValueError("Date string is empty. The correct format is 'YYYY-MM-DD'.")
    try:
        today = datetime.today()
        provided_date = parse_date_from_string(date)
        day_difference = (today - provided_date).days

        return day_difference
    except ValueError as e:
        raise ValueError(f"Error processing the date: {e}")



if __name__ == "__main__":
    mock_date = '2024-10-11'
    print(get_days_from_today(mock_date))

