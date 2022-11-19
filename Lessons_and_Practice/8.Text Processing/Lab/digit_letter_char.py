some_string = input()
digits = []
letter = []
char = []
for current_char in some_string:
    if current_char.isdigit():
        digits.append(current_char)
    elif current_char.isalpha():
        letter.append(current_char)
    else:
        char.append(current_char)

print(f"{''.join(digits)}\n{''.join(letter)}\n{''.join(char)}")