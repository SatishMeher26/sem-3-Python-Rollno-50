import re

# Email pattern
EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'


# Find all emails from a block of text
def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)


# Validate one email address
def is_valid_email(candidate):
    return re.fullmatch(EMAIL_PATTERN, candidate) is not None


# Main program
if __name__ == "__main__":

    sample_text = """
    Please contact us for support:
    - General queries: support@examplecorp.com
    - Sales team: sales.team@business-hub.co.in
    - Personal note from Rahul: rahul_23@gmail.com
    - Invalid mentions: not-an-email, @missing-local.com, plain.text@
    - Newsletter: newsletter+promo@my-site.org
    """

    print("Original text:")
    print(sample_text)

    # Find emails
    found = find_emails(sample_text)

    print("Found", len(found), "email address(es):")

    for email in found:
        print("-", email)

    # Validate individual emails
    print("\nValidating individual email addresses:")

    test_cases = [
        "john.doe@example.com",
        "invalid-email",
        "user@site",
        "user@site.com",
        "plain.text@",
        "a.b-c_d+e@sub.domain.co.in"
    ]

    for candidate in test_cases:
        if is_valid_email(candidate):
            print(candidate, "-> VALID")
        else:
            print(candidate, "-> INVALID")