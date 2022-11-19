# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.
# 3, 2, 1, 5, 8	[1, 4]


nums_in_string = input().split(", ")
list_num = list(map(int, nums_in_string))

# even_num = [num for num in range(len(list_num)) if list_num[num] % 2 == 0]
# even = list(map(lambda num: list_num.index(num), list(filter(lambda num: num % 2 == 0, list_num))))
even = list(map(lambda num: num, list(filter(lambda num: num % 2 == 0, list_num))))

print(even)