# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors.
# Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end.
# For example: "XXXXX 4" (5 chairs and 4 visitors).

def free_rooms_in_office(rooms):
    free_rooms = 0
    total_free_chairs = 0
    for room in range(number_of_rooms):

        current_room = room + 1
        chairs, visitors = input().split(" ")
        if len(chairs) >= int(visitors):
            diff = len(chairs) - int(visitors)
            free_rooms += 1
            total_free_chairs += diff
        else:
            needed_chairs_in_room = int(visitors) - len(chairs)
            print(f"{needed_chairs_in_room} more chairs needed in room {current_room}")
    if free_rooms == number_of_rooms:
        print(f"Game On, {total_free_chairs} free chairs left")



number_of_rooms = int(input())
result = free_rooms_in_office(number_of_rooms)


