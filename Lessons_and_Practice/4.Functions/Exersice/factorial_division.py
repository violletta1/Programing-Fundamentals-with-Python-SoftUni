# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.


def division_of_two_sums(num_one, num_two):
    sum_of_num_one = num_one
    sum_of_num_two = num_two
    for num in range(1, num_one):
        sum_of_num_one *= num
    for num in range(1, num_two):
        sum_of_num_two *= num
    return sum_of_num_one // sum_of_num_two




first_number = int(input())
second_number = int(input())
result = division_of_two_sums(first_number, second_number)
print(f"{result:.2f}")
