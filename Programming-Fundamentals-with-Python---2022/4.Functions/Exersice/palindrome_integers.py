# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.

def palindrome_check(number):
    return int(number) == int(number[::-1])


list_of_numbers = input().split(", ")

for number in list_of_numbers:
    print(palindrome_check(number))


# def is_polindrome(number):
#     return number == number[::-1]
#
#
# numbers = input().split(", ")
#
# for number in numbers:
#     print(is_polindrome(number))