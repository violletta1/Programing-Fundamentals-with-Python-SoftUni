import math

# def center_point(x1, y1, x2, y2):
#     return (x2 - x1)**2 + (y2-y1)**2
#
#
# first_number = float(input())
# second_number = float(input())
# third_number = float(input())
# four_number = float(input())
# dist_first_second = center_point(first_number, second_number, 0, 0)
# dist_third_four = center_point(third_number, four_number, 0, 0)
# dist = center_point(first_number, second_number, third_number, four_number)
#
# if dist_first_second < dist_third_four:
#     print(f"({math.floor(first_number)}, {math.floor(second_number)})")
# elif dist_third_four <= dist_first_second:
#     print(f"({math.floor(third_number)}, {math.floor(four_number)})")
# print(dist_first_second)
# print(dist)
# print(dist_third_four)

#
#
#
#
# import math
#
#
# def get_distance(_x1, _y1, _x2, _y2):
#     return math.sqrt(math.pow(_x2 - _x1, 2.0) + math.pow(_y2 - _y1, 2.0))
#
#
# x1 = math.floor(float(input()))
# y1 = math.floor(float(input()))
# x2 = math.floor(float(input()))
# y2 = math.floor(float(input()))
#
# dist1 = get_distance(x1, y1, 0, 0)
# dist2 = get_distance(x2, y2, 0, 0)
#
# if dist1 <= dist2:
#     print(f"({x1}, {y1})")
# else:
#     print(f"({x2}, {y2})")


import math

def center_point(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2-y1)**2


first_number = float(input())
second_number = float(input())
third_number = float(input())
four_number = float(input())
dist_first_second = center_point(first_number, second_number, 0, 0)
dist_third_four = center_point(third_number, four_number, 0, 0)

if dist_first_second < dist_third_four:
    print(f"({math.floor(first_number)}, {math.floor(second_number)})")
elif dist_third_four <= dist_first_second:
    print(f"({math.floor(third_number)}, {math.floor(four_number)})")
