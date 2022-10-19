# Write a program that receives a sequence of numbers (a string containing integers separated by ", ")
# and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# The numbers 2, 8, 4, and 10 fall into the group of 10's.
# The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.


#
# sequence_of_numbers = [int(sequence) for sequence in input().split(", ")]
# boundary = 0
# for current_number in range(len(sequence_of_numbers)):
#     boundary += 10
#     current_number, boundary


numbers = [int(number) for number in input().split(", ")]  #разделяме числата и си превръщаме от стринг в инт
group_of_numbers = 10                   # започваме сортиането на числа с критерий от 0 до 10
counter = 0                             #позиция на текушото число
while counter < len(numbers):          # проверяваме докато позицията на текушото число не надвишава броя на числа(все оше има числа)
    collected_numbers = []                    #лист в който ште събираме числата според категория (зануляваме го преди проверка на текушото сортиране )
    for number in numbers:            #за текушото число от лист с числа
        if group_of_numbers - 10 < number <= group_of_numbers:           # ако числото е по голямо от предходното сортиране и е по малко или равно от текушото
            collected_numbers.append(number)                                # добави го към листа с числа към текушото сортиране
            counter += 1                                                    # премини към следвашата позиия на дадено число от листта с числа
    print(f"Group of {group_of_numbers}'s: {collected_numbers}")           #след проверката на всички числа за даденото сортиране принтирай сортирането и листа с добавени числа
    group_of_numbers += 10             #увеличаваме критерия за сортиране на числа с 10