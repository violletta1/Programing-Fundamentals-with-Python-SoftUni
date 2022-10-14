
def multiplications(num1, num2, num3):
    zero_valid = False
    negative_valid = False
    positive_valid = False
    list_of_nums = [num1, num2, num3]
    for number in list_of_nums:
        number = int(number)
        if number == 0:
            zero_valid = True
            break
        if number < 0:
            negative_valid = True
        if number > 0:
            positive_valid = True
    if zero_valid:
        return "zero"
    if negative_valid:
        return "negative"
    if positive_valid:
        return "positive"



num_one = input()
num_two = input()
num_three = input()

result = multiplications(num_one, num_two, num_three)
print(*result)