#
# ⦁	"add {people}" – you should add the number of people in the last wagon
# ⦁	"insert {index} {people}" - you should add the number of people at the given wagon
# ⦁	"leave {index} {people}" - you should remove the number of people from the wagon.
# There will be no case in which the people will be more than the count in the wagon.

num_of_wagons = int(input())
train = [0] * num_of_wagons

command = input()
while not command == "End":
    data = command.split()
    if "add" in data:
        train[-1] += int(data[1])

    elif "insert" in data:
        train[int(data[1])] += int(data[2])

    elif data[0] == "leave":
        train[int(data[1])] -= int(data[2])


    command = input()


print(train)