# You will be receiving names of students, their ID, and a course of programming they have taken in the format "{name}:{ID}:{course}".
# On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format: "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique
students = {} # създаваме речник

command = input().split(":")# разделяме на елементи зададената команда чрез ":"
#
while len(command) > 1:# докато командата е с повече от 1 елемент
    name, id, course = command[0], command[1], command[2]# разделяме командата на 3 части списък

    if course not in students.keys():# ако дадена част от командата(определна за клуч) не е част от ключовете на създадения речник
        students[course] = []#създаваме елемент с клуч(елемента от подадената команда) и стойност празен списък
    students[course].append(f"{name} - {id}")# добавяме още иформация към стойността на клуча

    command = input().split(":")#

searched_course = command[0].replace("_", " ")# при излизане от while цикъл правим променлива със стойност - първият елемент от зададената команда превърната в списък
#първи начин
# print("\n".join(students[searched_course]))#изважда стойноста на дадения ключ(searched_course) \n разделя на отделен ред елементите от списъка
# #втори начин
for student in students[searched_course]: #минава през всеки елемент от спиъка в даден еемент в речник с [ключ]
    print(student)



# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals