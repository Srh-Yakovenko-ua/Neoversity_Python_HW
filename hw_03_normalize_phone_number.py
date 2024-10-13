import re

# Regular expression pattern for phone number matching

phone_pattern = r"^(380|80|0)?(\d{9})(\d*)$"
country_code = "+380"
non_digit_pattern = r"\D"
second_group_reference = r"\2"
def normalize_to_ukraine_format(phone_number: str) -> str:
    """
      Normalizes a phone number to the Ukraine format by applying a regex.

      Args:
          phone_number (str): The raw phone number.

      Returns:
          str: The normalized phone number with Ukraine's country code.
      """
    return re.sub(phone_pattern, country_code + second_group_reference, phone_number)



def normalize_phone(phone_number: str) -> str:
    """
       Cleans and normalizes a phone number by removing non-digit characters and
       converting it to the Ukraine format.

       Args:
           phone_number (str): The raw phone number.

       Returns:
           str: The normalized phone number or an empty string if invalid.
       """
    try:
        phone_number = str(phone_number)
        # Remove all non-digit characters
        phone_number = re.sub(non_digit_pattern, "", phone_number)

        # Check if the phone number is valid (must have at least 9 digits)
        if len(phone_number) < 9:
            return ""


        return normalize_to_ukraine_format(phone_number)


    except (TypeError, ValueError):
        return ""


if __name__ == "__main__":
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Normalized phone numbers for SMS distribution:", sanitized_numbers)





