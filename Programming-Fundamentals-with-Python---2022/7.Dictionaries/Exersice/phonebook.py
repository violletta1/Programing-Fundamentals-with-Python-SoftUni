# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format: "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."
# searched_course = command[0].replace("_", " ")

phonebook = {}
command = input().split("-")


while len(command) > 1:
    name, number = command[0], command[1]
    phonebook[name] = number
    command = input().split("-")

num_of_people_for_searched = command[0]

for searched_person in range(int(num_of_people_for_searched)):
    current_person = input()
    if current_person in phonebook.keys():
        print(f"{current_person} -> {phonebook[current_person]}")
    else:
        print(f"Contact {current_person} does not exist.")
