
key = int(input())
number_of_letters = int(input())
need_decrypt_word = ""
for index in range(number_of_letters):
    current_letter = input()
    need_decrypt_word += current_letter

decrypt_word = ""

for letter in need_decrypt_word:
    new_letter = chr(ord(letter) + key)
    decrypt_word += new_letter

print(decrypt_word)

# for letter in need_decrypt_word:
#     new_position = (alphabets.find(letter) + key) % len(alphabets)
#     decrypt_word += alphabets[new_position]
