# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers.
# Use filter().
#


def even_numbers(numbers):
    filtered_even_nums = []
    for number in numbers:
        number = int(number)
        if number % 2 == 0:
            filtered_even_nums.append(number)
    return filtered_even_nums


list_of_numbers = input().split(" ")

result = even_numbers(list_of_numbers)
print(result)


