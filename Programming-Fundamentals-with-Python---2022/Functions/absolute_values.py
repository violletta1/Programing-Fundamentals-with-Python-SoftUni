
def abs_digits_from_console(list_of_numbers):
    for number in list_of_numbers:
        check_number = isinstance(number, int)
        if check_number == True:
            number = abs(int(number))
        else:
            number = abs(float(number))





        abs_list_of_numbers.append(number)
    return abs_list_of_numbers



abs_list_of_numbers = []
numbers = input().split(" ")

result = abs_digits_from_console(numbers)
print(result)
