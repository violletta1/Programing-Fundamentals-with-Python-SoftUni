time_of_two_cars = [int(x) for x in input().split(" ")]

finish_point = len(time_of_two_cars) // 2
left_car_race = time_of_two_cars[0:finish_point]
right_car_race = time_of_two_cars[-1:finish_point:-1]
total_left_car = 0
total_right_car = 0
for current_left_time in left_car_race:
    total_left_car += current_left_time
    if current_left_time == 0:
        total_left_car *= 0.8
for current_right_time in right_car_race:
    total_right_car += current_right_time
    if current_right_time == 0:
        total_right_car *= 0.8


if total_right_car < total_left_car:
    print(f"The winner is right with total time: {total_right_car:.1f}")
else:
    print(f"The winner is left with total time: {total_left_car:.1f}")
