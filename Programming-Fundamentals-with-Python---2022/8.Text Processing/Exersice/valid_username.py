
def no_redundant_symbols(current_string):
    if ' ' in current_string:
        return False
    return True



def valid_char(current_string):
    for character in current_string:
        if not (character.isalnum() or character == "_" or character == "-"):
            return False
    return True



def valid_length(current_string):
    if 3 < len(current_string) < 16:
        return True
    return False

def is_valid(some_sting):
    valid_string = []
    for current_string in some_sting:
        if no_redundant_symbols(current_string) and valid_length(current_string) and valid_char(current_string):
            valid_string.append(current_string)
    return "\n".join(valid_string)


list_of_usernames = input().split(", ")

valid_usernames = is_valid(list_of_usernames)
print(valid_usernames)