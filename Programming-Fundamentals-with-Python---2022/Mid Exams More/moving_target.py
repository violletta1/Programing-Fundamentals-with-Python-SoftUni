def check_if_index_is_valid(index, len_list):
    if index in range(len_list):
        return True
    return False


targets = [int(el) for el in input().split()]

command_data = input()

while not command_data == "End":
    command, index, val = command_data.split()
    index = int(index)
    val = int(val)
    if command == "Shoot":
        if check_if_index_is_valid(index, len(targets)):
            targets[index] -= val
            if targets[index] <= 0:
                targets.pop(index)
    elif command == "Add":
        if check_if_index_is_valid(index, len(targets)):
            targets.insert(index, val)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        left_most_index = index - val
        right_most_index = index + val
        if check_if_index_is_valid(index, len(targets)) and check_if_index_is_valid(left_most_index, len(targets)) and check_if_index_is_valid(right_most_index, len(targets)):
            left_unstriked_part = targets[:left_most_index]
            right_unstriked_part = targets[right_most_index + 1:]
            targets = left_unstriked_part + right_unstriked_part
        else:
            print("Strike missed!")

    command_data = input()

print('|'.join([str(el) for el in targets]))



def index_valid(some_index, len_list):
    if some_index in range(len_list):
        return True
    return False


targets = [int(target) for target in input().split()]

command = input()
while not command == "End":
    command, index, value = command.split()
    index = int(index)
    value = int(value)
    if command == "Shoot":
        if index_valid(index, len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif command == "Add":
        if index_valid(index, len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")


    elif command == "Strike":
        left_side_index = index - value   # we need to know the index of the elements in radius
        right_side_index = index + value
        if index_valid(index, len(targets)) and index_valid(left_side_index, len(targets)) and index_valid(right_side_index, len(targets)):   # if the index from radius of current index is valid (in len of the list)
            left_el = targets[:left_side_index]                 #save the elements at left and right side without the elements in given radius
            right_el = targets[right_side_index+1:]
            targets = left_el + right_el
        else:
            print("Strike missed!")


    command = input()

print("|".join([str(target) for target in targets]))