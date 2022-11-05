# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].

command = input()
miner = {} # създаваме празен речник

list_string = []

while command != "stop":
    list_string.append(command)

    command = input()

for index in range(0, len(list_string), 2):# преминаваме през веки ВТОРИ елемент (със стъпка 2)от списъка

    resourse = list_string[index]# задаваме стойност на ключа
    if resourse in miner.keys():
        quantity = int(list_string[index + 1])
        miner[resourse] += quantity
    else:
        quantity = int(list_string[index + 1])
        miner[resourse] = int(list_string[index + 1]) # посоваме кой елемент заема място на стойнот към ключ от предходен индекс

for resourse, quantity in miner.items():# за всеки ключ,ст-ст в елементите на речника (чрезз метод enumerate)
    print(f"{resourse} -> {quantity}")#