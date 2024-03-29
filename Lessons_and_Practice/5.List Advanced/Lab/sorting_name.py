# Write a program that reads a single string with names separated by comma and space ", ".
# Sort the names by their length in descending order.
# If 2 or more names have the same length, sort them in ascending order (alphabetically). Print the resulting list.
names = input().split(", ")
list_of_names = sorted(names, key=lambda name: (-len(name), name))
# list_of_names = sorted(names, key=lambda name: len(name), names)

print(list_of_names)