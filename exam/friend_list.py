friends = input().split(", ")

blacklisted_names = 0
lost_name = 0
command = input()

while command != "Report":
    if "Blacklist" in command:
        task, name = command.split()
        if name in friends:
            index = friends.index(name)
            friends[index] = "Blacklisted"
            blacklisted_names += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    if "Error" in command:
        task, index = command.split()
        index = int(index)
        if 0 <= index < len(friends) and friends[index] != "Blacklist" and friends[index] != "Lost":
            name = friends[index]
            friends[index] = "Lost"
            lost_name += 1
            print(f"{name} was lost due to an error.")
        else:
            command = input()
            continue
    if "Change" in command:
        task, index, new_name = command.split()
        index = int(index)
        if 0 <= index < len(friends):
            current_name = friends[index]
            friends[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")
        else:
            command = input()
            continue



    command = input()

print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_name}")
print(" ".join(friends))

