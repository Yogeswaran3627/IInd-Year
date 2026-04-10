## Problem: Email Validation
Write a script to validate an email address based on specific character rules.

def is_valid_email(email):
    # 1. No spaces allowed
    if " " in email:
        return False

    # 2. Exactly one '@'
    if email.count("@") != 1:
        return False
    local, domain = email.split("@")

    # 3. Local and domain parts must not be empty
    if not local or not domain:
        return False

    # 4. Local part checks
    if local.startswith(".") or local.endswith("."):
        return False
    if " .. " in local:
        return False

    allowed_local_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-"
    for char in local:
        if char not in allowed_local_chars:
            return False

    # 5. Domain part checks
    if domain.startswith(".") or domain.endswith("."):
        return False
    if " .. " in domain:
        return False
    if "." not in domain:
        return False

    domain_parts = domain.split(".")

    # 6. Each domain label must be alphanumeric
    for part in domain_parts:
        if not part.isalnum():
            return False

    # 7. TLD length check
    if len(domain_parts[-1]) < 2:
        return False

    return True


email = input("Enter email address: ")

if is_valid_email(email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")

## Sample Input/Output
- **Input:** `test.user@gmail.com`
- **Output:** `Valid Email Address`

- **Input:** `test..user@com`
- **Output:** `Invalid Email Address`
