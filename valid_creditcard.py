import re

def validate_credit_card(number):
    # Remove any hyphens from the number
    number = number.replace("-", "")

    # Check if the number starts with a valid prefix
    if not re.match(r"^[456]", number):
        return "Invalid"

    # Check if the number has exactly 16 digits
    if not re.match(r"^[456]\d{15}$", number):
        return "Invalid"

    # Check if the number only consists of digits
    if not re.match(r"^\d+$", number):
        return "Invalid"

    # Check if the number has groups of 4 digits separated by hyphens
    if not re.match(r"^\d{4}(-?\d{4}){3}$", number):
        return "Invalid"

    # Check if the number has no more than 3 consecutive repeated digits
    if re.search(r"(\d)\1{3}", number):
        return "Invalid"

    return "Valid"


# Get the number of credit card inputs
n = int(input())

# Validate each credit card number and print the result
for _ in range(n):
    card_number = input()
    print(validate_credit_card(card_number))
