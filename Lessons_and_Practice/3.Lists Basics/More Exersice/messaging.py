numbers_list = input().split(' ')
message = input()
secret_message = []

for number in numbers_list:
    sum_of_current_digit = 0
    for digit in number:
        sum_of_current_digit += int(digit)

    sum_of_current_digit %= len(message)

    secret_message.append(message[sum_of_current_digit])
    message = list(message)
    message.pop(sum_of_current_digit)

print("".join(secret_message))
print(type(secret_message))