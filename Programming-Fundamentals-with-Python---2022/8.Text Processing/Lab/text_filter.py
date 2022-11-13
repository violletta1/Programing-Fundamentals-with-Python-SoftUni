string_of_banned_words = input().split(", ")
text = input()

for current_word in string_of_banned_words:
    while current_word in text:
        text = text.replace(current_word, "*" * len(current_word))

print(text)