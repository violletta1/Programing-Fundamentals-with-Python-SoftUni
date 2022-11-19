# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
# and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number
# Input
# 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33	                    # 1, 2, 53, 2, 21
# Output
# Positive: 1, 0, 5, 3, 4, 12, 19                                 # Positive: 1, 2, 53, 2, 21
# Negative: -2, -100, -20, -33                                   # Negative:
# Even: -2, 0, 4, -100, -20, 12                                 # Even: 2, 2
# Odd: 1, 5, 3, 19, -33                                         # Odd: 1, 53, 21



def positive(sum_nums):
    filtered_positive = ", ".join([str(num) for num in sum_nums if num >= 0])
    return filtered_positive

def negative(sum_nums):
    filtered_negative = ", ".join([str(num) for num in sum_nums if num < 0])
    return filtered_negative

def even(sum_nums):
    even_nums = []
    for num in sum_nums:
        if num % 2 == 0:
            even_nums.append(num)
    return ", ".join([str(num) for num in even_nums])

def odd(sum_nums):
    filtered_off = ", ".join([str(num) for num in sum_nums if num % 2 != 0])
    return filtered_off

numbers = [int(number) for number in input().split(",")]

print(f"Positive: {positive(numbers)}")
print(f"Negative: {negative(numbers)}")
print(f"Even: {even(numbers)}")
print(f"Odd: {odd(numbers)}")