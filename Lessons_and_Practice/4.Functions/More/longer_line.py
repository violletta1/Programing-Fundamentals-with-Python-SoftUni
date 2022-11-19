import math

def center_point(x1, y1, x2, y2):

    return math.floor(x2 - x1)**2 + (y2 - y1)**2

first_number = float(input())
second_number = float(input())
third_number = float(input())
fourth_number = float(input())
fifth_number = float(input())
sixth_number = float(input())
seventh_number = float(input())
eight_number = float(input())

dist_first_second = center_point(first_number, second_number, 0, 0)
dist_third_four = center_point(third_number, fourth_number, 0, 0)
dist_fifth_sixth = center_point(fifth_number, sixth_number, 0, 0)
dist_seventh_eight = center_point(seventh_number, eight_number, 0, 0)

first_line = math.floor(dist_first_second + dist_third_four)
second_line = math.floor(dist_fifth_sixth + dist_seventh_eight)

if first_line >= second_line:
    if dist_first_second <= dist_third_four:
        print(f"({math.floor(first_number)}, {math.floor(second_number)})({math.floor(third_number)}, {math.floor(fourth_number)})")
    else:
        print(f"({math.floor(third_number)}, {math.floor(fourth_number)})({math.floor(first_number)}, {math.floor(second_number)})")

if second_line > first_line:
    if dist_fifth_sixth <= dist_seventh_eight:
        print(f"({math.floor(fifth_number)}, {math.floor(sixth_number)})({math.floor(seventh_number)}, {math.floor(eight_number)})")
    else:
        print(f"({math.floor(seventh_number)}, {math.floor(eight_number)})({math.floor(fifth_number)}, {math.floor(sixth_number)})")
