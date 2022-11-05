# "multiply", "divide", "add", "subtract".

def active_action(mathematic, num1, num2):
    if mathematic == "multiply":
        return num1 * num2
    elif mathematic == "divide":
        return num1 // num2
    elif mathematic == "add":
        return num1 + num2
    elif mathematic == "subtract":
        return num1 - num2




action = input()
first_number = int(input())
second_number = int(input())
result = active_action(action, first_number, second_number)
print(result)