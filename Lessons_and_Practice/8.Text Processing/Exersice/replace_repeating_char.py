# Write a program that reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.
#Input: aaaaabbbbbcdddeeeedssaa
#Output: abcdedsa
text = input()
replaced_text = []
last_letter = ""
for current_letter in text:
    if current_letter != last_letter:
        replaced_text.append(current_letter)
        last_letter = current_letter

print("".join(replaced_text))


#
# some_text = input()
# final_text = ""
# last_letter = ""
# for current_letter in some_text:
#     if current_letter != last_letter:
#         final_text += current_letter
#         last_letter = current_letter
# print(final_text)