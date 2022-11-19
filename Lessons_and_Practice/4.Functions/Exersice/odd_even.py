#You will receive a single number.
# You should write a function that returns the sum of all even and all odd digits in a given number.
# The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.


def sum_of_even_and_off(number):
    sum_of_even = 0
    sum_of_odd = 0
    for current_digit in number:
        current_digit = int(current_digit)
        if current_digit % 2 == 0:
            sum_of_even += current_digit
        else:
            sum_of_odd += current_digit
    return sum_of_odd, sum_of_even

received_number = input()
sum_of_odd_digits, sum_of_even_digits = sum_of_even_and_off(received_number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")

