number_of_electrons = int(input())
filled_shells = []
current_shell = 0

while 0 < number_of_electrons:

    current_shell += 1
    shell_capacity = 2 * current_shell ** 2

    if number_of_electrons >= shell_capacity:
        filled_shells.append(shell_capacity)
        number_of_electrons -= shell_capacity
    else:
        filled_shells.append(number_of_electrons)
        number_of_electrons = 0

print(filled_shells)