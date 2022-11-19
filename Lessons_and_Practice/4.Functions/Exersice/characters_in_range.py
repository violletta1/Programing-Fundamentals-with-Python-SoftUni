

def characters_in_range(char_one, char_two):
    for current_char in range(ord(char_one) + 1, ord(char_two)):
        all_chars.append(chr(current_char))
    return all_chars


first_char = input()
second_char = input()
all_chars = []
result = characters_in_range(first_char, second_char)
print(*result)