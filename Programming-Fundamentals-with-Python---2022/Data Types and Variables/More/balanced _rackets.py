

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
