# You will receive three integer numbers.
# Write functions named:
# sum_numbers() that returns the sum of the first two integers
# subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.


def sum_numbers(first_num, second_num):
    return first_num + second_num



def subtract(sum_numbers, third_num):
    return sum_numbers - third_num



def add_and_subtract(first_num, second_num, third_num):
    sum_nums = sum_numbers(first_num, second_num)
    diff = subtract(sum_nums, third_num)
    return diff


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = add_and_subtract(first_number, second_number, third_number)
print(result)