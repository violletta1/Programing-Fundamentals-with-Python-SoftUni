#
some_text = input()
new_text = ""
strength = 0
for index in range(len(some_text)):
    if strength > 0 and some_text[index] != ">":
        strength -= 1
    elif some_text[index] == ">":
        new_text += some_text[index]
        strength += int(some_text[index + 1])
    else:
        new_text += some_text[index]
print(new_text)


# some_string = input()
# explosed_sting = []
#
# for index in range(len(some_string)):
#     if some_string[index] != ">":
#         continue
#     elif some_string[index] == ">":
#         quantity_remove_index = int(some_string[index + 1])
#         for remove_index in range(quantity_remove_index):
#         # explosed_sting[index] =
#
#
#
#     if some_string[index] != ">":
#         explosed_sting.append(some_string[index])
#     elif some_string[index] == ">":
#         explosed_sting.append(some_string[index])
#         index = 1 + (index + int(some_string[index + 1]))
# print("".join(explosed_sting))