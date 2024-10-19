import re

def validate_phone_number(phone):
    """Validate a phone number."""
    phone_pattern = re.compile(r"^(\+1[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}$")
    return bool(phone_pattern.match(phone))

def validate_ssn(ssn):
    """Validate a Social Security Number (SSN)."""
    ssn_pattern = re.compile(r"^\d{3}-\d{2}-\d{4}$")
    return bool(ssn_pattern.match(ssn))

def validate_zip_code(zip_code):
    """Validate a zip code."""
    zip_pattern = re.compile(r"^\d{5}(-\d{4})?$")
    return bool(zip_pattern.match(zip_code))

def main():
    """Main function to get user input and validate the data."""
    phone = input("Enter a phone number: ")
    ssn = input("Enter a Social Security Number (SSN): ")
    zip_code = input("Enter a ZIP code: ")
    
    # Validate phone number
    if validate_phone_number(phone):
        print(f"Phone number '{phone}' is valid.")
    else:
        print(f"Phone number '{phone}' is invalid.")
    
    # Validate SSN
    if validate_ssn(ssn):
        print(f"SSN '{ssn}' is valid.")
    else:
        print(f"SSN '{ssn}' is invalid.")
    
    # Validate ZIP code
    if validate_zip_code(zip_code):
        print(f"ZIP code '{zip_code}' is valid.")
    else:
        print(f"ZIP code '{zip_code}' is invalid.")

# Test the functions
if __name__ == "__main__":
    main()
