# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"
some_string = input().split()# поставяме дъмата в списък

letter_string = "".join(some_string)#превръщме в стринг в който можем да проверяваме всеки елемент от думата

dict_letter_occurrences = {}#създаваме речник

for symbol in letter_string:# за всеки елемент от стринга (думата)
    if symbol not in dict_letter_occurrences.keys():# ако елемента  не е в речника

        dict_letter_occurrences[symbol] = 1#създаваме елемент в речника
    else:#ако елемента е в речника
        dict_letter_occurrences[symbol] += 1# увеличаваме ст-ста на клюЧА

for element, occurrences in dict_letter_occurrences.items():# за всеки ключ,ст-ст в елементите на речника (чрезз метод enumerate)
    print(f"{element} -> {occurrences}")#