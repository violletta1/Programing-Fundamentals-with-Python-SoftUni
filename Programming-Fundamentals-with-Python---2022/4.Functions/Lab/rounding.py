import math
def transform_float_to_int(list_of_float):
    for digit in list_of_float:
        digit = round(float(digit))

        list_of_int.append(digit)
    return list_of_int



list_of_digit = input().split(" ")
list_of_int = []
result = transform_float_to_int(list_of_digit)
print(result)