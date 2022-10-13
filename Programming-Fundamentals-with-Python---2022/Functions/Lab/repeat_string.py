# Write a function that receives a string and a counter n.
# The function should return a new string – the result of repeating the old string n times.
# Print the result of the function. Try using lambda.

#
def repeated_text(text, times_repeat):
    return text * times_repeat


text_from_user = input()
number_of_repeating = int(input())
print(repeated_text(text_from_user, number_of_repeating))


#

# text_from_user = input()
# number_of_repeating = int(input())
#
#
# repeated_text = lambda a, b: a * b
#
# result = repeated_text(text_from_user, number_of_repeating)
# print(result)