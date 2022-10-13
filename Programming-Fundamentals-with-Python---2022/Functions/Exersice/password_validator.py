# "Password must be between 6 and 10 characters"
# "Password must consist only of letters and digits"
# "Password must have at least 2 digits"


def password_check(some_string):
    valid_password = True
    if len(some_string) < 6 or len(some_string) > 10:
        valid_password = False
        print("Password must be between 6 and 10 characters")
    if not some_string.isalnum():
        valid_password = False
        print("Password must consist only of letters and digits")
        # digit_count = [digit for digit in some_string if digit.isdigit()]
        # if len(digit_count) < 2:
        #     valid_password = False
        #     print("Password must have at least 2 digits")
    digits = 0
    for digit in some_string:
        if digit.isdigit():
            digits += 1
    if digits < 2:
        valid_password = False
        print("Password must have at least 2 digits")
    return valid_password


password = input()

result = password_check(password)

if result:
    print('Password is valid')