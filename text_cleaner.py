# Text-Cleanup Utilities for Enterprise Pipelines
# Author: Pavan
# Week 02 Deliverable: Python Core & Functions

def clean_text(raw_text):
    """
    Strips leading and trailing whitespace from a dirty string.
    """
    return raw_text.strip()

def clean_phone_number(raw_phone):
    """
    Extracts only digits from formatted phone strings (e.g. '+1 (555) 019-2834' -> '15550192834').
    """
    digits_only = ""
    for char in raw_phone:
        if char.isdigit():
            digits_only += char
    return digits_only

def clean_currency(raw_money):
    """
    Sanitizes currency strings ($1,450.75 USD) and safely converts them to floats.
    Returns 0.0 on corrupt/non-numeric inputs without crashing.
    """
    cleaned_str = raw_money.replace("$", "").replace(",", "").replace("USD", "").strip()
    try:
        return float(cleaned_str)
    except ValueError:
        return 0.0

if __name__ == "__main__":
    # Test 1: Clean text
    test_str = "    Forward Deployed Engineer    "
    print(f"Clean Text : '{clean_text(test_str)}'")

    # Test 2: Clean phone number
    test_phone = "+1 (555) 019-2834"
    print(f"Clean Phone: '{clean_phone_number(test_phone)}'")

    # Test 3: Clean currency (Valid)
    test_money = "$1,450.75 USD"
    print(f"Clean Money: {clean_currency(test_money)}")

    # Test 4: Clean currency (Corrupt edge case)
    test_corrupt = "FREE_PRICE_N/A"
    print(f"Corrupt Safe Fallback: {clean_currency(test_corrupt)}")
