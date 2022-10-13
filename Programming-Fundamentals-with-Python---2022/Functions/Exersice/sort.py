# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().

# 6 4 2

def sorted_numbers(numbers):
    list_digit_nums = [int(item) for item in numbers]
    sorted_num = sorted(list_digit_nums)
    return sorted_num


list_num = input().split(" ")
sort_nums = sorted_numbers(list_num)
print(sort_nums)