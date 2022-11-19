
from collections import defaultdict



courses = {}

course_name = input().split(" : ")

while len(course_name) > 1:
    type_course = course_name[0]
    name = course_name[1]
    if type_course not in courses.keys():
        courses[type_course] = [name]
    else:
        courses[type_course].append(name)

    course_name = input().split(" : ")

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for el in value:
        print(f"-- {el}")