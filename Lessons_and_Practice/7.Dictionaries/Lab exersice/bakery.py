
# You will receive a single line containing some food (keys) and quantities (values).
# They will be separated by a single space (the first element is the key, the second – the value, and so on).
# Create a dictionary with all the keys and values and print it on the console.


grocery = input().split() # създаваме списък от дадения вход и го разделяме по празно място
# print(grocery)

bakery = {} # създаваме празен речник

for index in range(0, len(grocery), 2): # преминаваме през веки ВТОРИ елемент (със стъпка 2)от списъка
    food = grocery[index] # задаваме стойност на ключа
    quantity = grocery[index + 1] # посоваме кой елемент заема място на стойнот към ключ от предходен индекс
    bakery[food] = int(quantity) # обузнаваме съдействие мейду клуч и стйност

print(bakery)




