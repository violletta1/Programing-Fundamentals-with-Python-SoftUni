

num_lines = int(input())
balanced = 0
all_strings = []
for current_string in range(num_lines):
    string = input()
    all_strings.append(string)
    if string == ")":
        if len(all_strings) == 0:
            print("UNBALANCED")
            break
    if string == "(":

        balanced += 1
        if balanced > 1:
            print("UNBALANCED")
            exit()
        if balanced == 0:
            print("BALANCED")
        else:
            continue
    elif string == ")":
        balanced -= 1

        if balanced < 0:
            print("UNBALANCED")
            exit()
        else:
            continue
    else:
        continue

if balanced == 0:
    print("BALANCED")


#
#
#
#
#
#
#
# lines = int(input())
#
# is_balanced = True
# last_bracket = ''
# for _ in range(0, lines):
#     current = input()
#     if current not in ['(', ')']:
#         continue
#
#     if last_bracket == '' and current == ')' or last_bracket == current:
#         is_balanced = False
#         break
#
#     last_bracket = current
#
# if is_balanced:
#     print('BALANCED')
# else:
#     print('UNBALANCED')
#
#
#
#
