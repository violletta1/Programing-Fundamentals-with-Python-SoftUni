# You will receive three integer numbers. Write a program that finds if their multiplication (the result) is negative, positive, or zero.
# Try to do this WITHOUT multiplying the 3 numbers.

def multiplications(num1, num2, num3):
    result = 1
    list_of_nums = [num1, num2, num3]
    for number in list_of_nums:
        number = int(number)
        result *= number
    if result == 0:
        return "zero"
    elif result < 0:
        return "negative"
    elif result > 0:
        return "positive"


num_one = input()
num_two = input()
num_three = input()

result = multiplications(num_one, num_two, num_three)
print(result)