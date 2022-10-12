numbers = input().split(", ")
list_of_num = []
counter_of_0 = 0

for current_number in numbers:
    if current_number == "0":
        counter_of_0 += 1
    else:
        list_of_num.append(int(current_number))



list_of_num.extend([0] * counter_of_0)
print(list_of_num)