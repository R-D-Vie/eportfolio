import re

def validate_uk_postcode(postcode):
    regex = r"^(GIR 0AA|[A-PR-UWYZ](?:[A-HK-Y]?[0-9]+|[0-9][A-HJKSTUW])? ?[0-9][ABD-HJLNP-UW-Z]{2})$"
    match = re.match(regex, postcode)
    return bool(match)

# Testing the validate_uk_postcode function
postcodes = ["M1 1AA", "M60 1NW", "CR2 6XH", "DN55 1PT", "W1A 1HQ", "EC1A 1BB"]
for postcode in postcodes:
    if validate_uk_postcode(postcode):
        print(f"{postcode} is a valid UK postcode.")
    else:
        print(f"{postcode} is not a valid UK postcode.")
