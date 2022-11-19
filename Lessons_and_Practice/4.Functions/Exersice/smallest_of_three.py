
def smallest_of_three_nums(numbers):
    min_num = min(numbers)
    return min_num


first_number = int(input())
second_number = int(input())
third_number = int(input())
list_of_nums = [first_number, second_number, third_number]
min_number = smallest_of_three_nums(list_of_nums)
print(min_number)