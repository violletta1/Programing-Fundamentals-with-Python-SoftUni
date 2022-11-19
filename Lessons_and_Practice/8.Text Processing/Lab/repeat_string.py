some_string = input().split()

multiply = []

for current_string in some_string:
    multiply.append(current_string * len(current_string))

print("".join(multiply))