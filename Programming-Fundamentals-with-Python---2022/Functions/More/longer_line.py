import math

def longer_line(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y1 - y2) ** 2

first_number = int(input())
second_number = int(input())
third_number = int(input())
fourth_number = int(input())
fifth_number = int(input())
sixth_number = int(input())
seventh_number = int(input())
eight_number = int(input())

result_1 = longer_line(first_number, second_number, 0, 0)
result_2 = longer_line(third_number, fourth_number, 0, 0)
result_3 = longer_line(fifth_number, sixth_number, 0, 0)
result_4 = longer_line(seventh_number, eight_number, 0, 0)

first_line = result_1 + result_2
second_line = result_3 + result_4

if first_line >= second_line:
    if result_1 <= result_2:
        print(f"({math.floor(first_number)}, {math.floor(second_number)})({math.floor(third_number)}, {math.floor(fourth_number)})")
    else:
        print(f"({math.floor(third_number)}, {math.floor(fourth_number)})({math.floor(first_number)}, {math.floor(second_number)})")
if second_line > first_line:
    if result_3 <= result_4:
        print(f"({math.floor(fifth_number)}, {math.floor(sixth_number)})({math.floor(seventh_number)}, {math.floor(eight_number)})")
    else:
        print(f"({math.floor(seventh_number)}, {math.floor(eight_number)})({math.floor(fifth_number)}, {math.floor(sixth_number)})")