# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print the min and max values of the given numbers and the sum of all the numbers in the list.
# Use min(), max() and sum().


def min_max_sum(numbers):
    list_of_digit_num = [int(x) for x in numbers]
    min_num = min(list_of_digit_num)
    max_num = max(list_of_digit_num)
    sum_num = sum(list_of_digit_num)
    return min_num, max_num, sum_num


list_of_num = input().split(" ")


minimum_number, maximum_number, sum_of_all_numbers = min_max_sum(list_of_num)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")
