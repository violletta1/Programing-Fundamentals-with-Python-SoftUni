# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.
students = {}
number_of_students = int(input())

for current_student in range(number_of_students):
    student = input()
    grade = float(input())

    if student not in students.keys():
        students[student] = [grade]
    else:
        students[student].append(grade)

students_copy = students.copy()
for student, grade in students_copy.items():
    average = sum(grade) / len(grade)
    if average < 4.50:
        students.pop(student)
    else:
        students[student] = average

for student, average in students.items():
    print(f"{student} -> {average:.2f}")