# Write a program that returns an encrypted version of the same text.
# Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII table.
# For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.



some_string = input()
encrypted_version = []

for current_char in some_string:
    ascii_char = ord(current_char)
    encrypted_version.append(chr(ascii_char + 3))

print("".join(encrypted_version))