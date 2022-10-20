

targets_list = [int(x) for x in input().split()]
new_list = []

command = input()

while command != "End":
    index_shooting = int(command)                                    #превръшаме стройността в число
    if index_shooting >= len(targets_list):#проверяваме зададения индекс дали е валиден спрямо дължината на списъка
        command = input()
        continue
    special_value = targets_list[index_shooting]   #ст-т на елемент от входящ индекс

    if targets_list[index_shooting] == -1:  # ако ел-та на зададеня индекс ет = -1
        command = input()
        continue
    targets_list[index_shooting] = -1            #премахни текушия ел и го замени със стойност -1

    for target in range(0, len(targets_list)):  # проверяваме всеки индекс на ел-т от списък
        if targets_list[target] == -1:  # ако ел-та на дадения индекс == -
            continue
        if targets_list[target] > special_value:  # ако ел-та на текушия индекс е по-голям или равно на елемента с  зададен индекс
            targets_list[target] -= special_value  # извади от ст-та на  текушия ел ст-та на зададения ел-т

        elif targets_list[target] <= special_value:  # and targets_list[target] != -1:        #ако текушия ел-т е по малък от зададения ел-т
            targets_list[target] += special_value  # добави стойността на зададения ел-т към текушия

    command = input()                                #  подай нова команда


result = " ".join(str(target) for target in targets_list)              #съедини листа с празно разтрояние
count_shoot_targets = targets_list.count(-1)                            # преброй даден елемент в списъка
print(f"Shot targets: {count_shoot_targets} -> {result}")                   ## print(f"Shot targets: {counter_shot_targets} -> {' '.join([str(el) for el in targets])}")

#
# targets = [int(el) for el in input().split()]
#
# index = input()
# counter_shot_targets = 0
#
# while not index == "End":
#     index = int(index)
#
#     if index not in range(len(targets)):
#         index = input()
#         continue
#
#     current_value = targets[index]
#
#     if current_value == -1:
#         index = input()
#         continue
#
#     targets[index] = -1
#     counter_shot_targets += 1
#
#     for current_index in range(len(targets)):
#         if targets[current_index] == -1:
#             continue
#         if targets[current_index] > current_value:
#             targets[current_index] -= current_value
#         else:
#             targets[current_index] += current_value
#
#     index = input()
#
# print(f"Shot targets: {counter_shot_targets} -> {' '.join([str(el) for el in targets])}")

