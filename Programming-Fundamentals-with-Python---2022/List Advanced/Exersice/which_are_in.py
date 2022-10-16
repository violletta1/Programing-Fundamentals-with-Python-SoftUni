first_string = input().split(", ")
second_string = input().split(", ")


substrings = [word for word in first_string if any(word in second_word for second_word in second_string)]
print(substrings)