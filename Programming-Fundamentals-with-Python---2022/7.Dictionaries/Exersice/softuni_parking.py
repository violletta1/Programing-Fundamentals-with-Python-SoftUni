register_people = {}

number_of_people = int(input())

for username in range(number_of_people):
    current_person = input().split()
    action = current_person[0]
    name = current_person[1]
    if action == "register":
        if name in register_people.keys():
            license_plate_number = register_people[name]
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            license_plate_number = current_person[2]
            register_people[current_person[1]] = license_plate_number
            print(f"{name} registered {license_plate_number} successfully")

    elif action == "unregister":
        if name not in register_people.keys():
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            register_people.pop(current_person[1])


for name, license_plate_number in register_people.items():
    print(f"{name} => {license_plate_number}")