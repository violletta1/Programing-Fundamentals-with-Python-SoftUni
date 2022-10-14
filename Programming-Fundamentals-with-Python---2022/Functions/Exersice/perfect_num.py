

def perfect_number(some_number):
    all_nums = 0
    some_number = int(some_number)
    for number in range(1, some_number):
        if some_number % number == 0:
            all_nums += number
        if all_nums == some_number:
            number_is_perfect = True
            return True
    return False

number = input()

result = perfect_number(number)
if result == True:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
