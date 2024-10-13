from datetime import datetime, timedelta


# Format of the date string
format_date = "%Y.%m.%d"

def parse_date_from_string(date: str) -> datetime.date:
    """
     Converts a string to a date object using the format 'YYYY.MM.DD'.

     Args:
         date (str): The date string to be parsed.

     Returns:
         datetime.date: The parsed date object.
     """
    return datetime.strptime(date, format_date).date()

def get_upcoming_birthdays(users_birthday: list[dict[str, str]]) -> list[dict[str, str]]:
    """
       Retrieves users whose birthdays are today or in the next 7 days.

       Args:
           users_birthday (list[dict[str, str]]): List of users with 'name' and 'birthday'.

       Returns:
           list[dict[str, str]]: List of users with upcoming birthdays and their congratulation date.
       """
    users_upcoming_birthday = []
    today = datetime.today().date()

    for user in users_birthday:
        try:
            birthday_date = parse_date_from_string(user["birthday"])
        except ValueError:
            continue # Skip users with invalid date format

        # Set the birthday to the current year
        birthday_this_year = birthday_date.replace(year=today.year)

        # Check if today is the user's birthday
        if birthday_this_year == today:
            users_upcoming_birthday.append(
                {
                    "name": user["name"],
                    "congratulation_date": "Today!",
                }
            )
            continue

        # If the birthday this year has already passed, set it to next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Check if the birthday is within the next 7 days
        if (birthday_this_year - today).days <= 7:
            # Adjust the birthday to avoid weekends
            while birthday_this_year.weekday() in [5, 6]:
                birthday_this_year += timedelta(days=1)

            users_upcoming_birthday.append(
                {
                    "name": user["name"],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
                }
            )

    return users_upcoming_birthday


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.10.13"},
        {"name": "Jane Smith", "birthday": "1990.07.07"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("List of congratulations for this week:", upcoming_birthdays)



