# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format: "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."
# searched_course = command[0].replace("_", " ")

phonebook = {}
command = input().split("-")


while len(command) > 1:# докато командата има повече от 1 ел-т
    name, number = command[0], command[1]#разделяме командата на части
    phonebook[name] = number#създаваме елемент в речника
    command = input().split("-")#

num_of_people_for_searched = command[0]#командата е 1 ел взимаме само 1та част

for searched_person in range(int(num_of_people_for_searched)):# за всеки човек в range от командата
    current_person = input()#взимаме от конзолатаа текущ човек
    if current_person in phonebook.keys():# ако текъщият човек съществува в речника
        print(f"{current_person} -> {phonebook[current_person]}")#
     else:#ако не съществува
        print(f"Contact {current_person} does not exist.")#



# phonebook = {}
# while True:
#     entry = input()
#     if "-" not in entry:
#         break
#     name, phone = entry.split("-")
#     phonebook[name] = phone
# for check in range(int(entry)):
#     searched_name = input()
#     if searched_name in phonebook.keys():
#         print(f"{searched_name} -> {phonebook[searched_name]}")
#     else:
#         print(f"Contact {searched_name} does not exist.")


