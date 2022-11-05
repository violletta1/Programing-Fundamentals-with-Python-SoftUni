# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...).
# Your task is to create a function that returns a loading bar depending on the number you have received in the input.
# Print the result on the console. For more clarification, see the examples below.


# 30	30% [%%%.......]
#       Still loading...
# 100	100% Complete!
#       [%%%%%%%%%%]\n

def loading_bar(some_number):
    if some_number == 100:
        return f"{some_number}% Complete!\n[{'%' * 10}]"
    return f"{some_number}% [{'%' * (some_number // 10)}{'.' * (10 - some_number // 10)}]\nStill loading..."

number = int(input())
result = loading_bar(number)
print(result)