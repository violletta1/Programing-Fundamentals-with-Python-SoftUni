# You are given a secret message you should decipher. To do that, you need to know that in each word:
# the second and the last letter are switched (e.g., Holle means Hello)
# the first letter is replaced by its character code (e.g., 72 means H)


def swap(word):

    word[1], word[-1] = word[-1], word[1]
    return word

text = input().split()

result = []

for current_word in text:
    list_digit = []
    deciher_word = []
    for element in current_word:
        if element.isdigit():
           list_digit.append(element)

    letter_in_ord = "".join(list_digit)
    letter_in_ord = chr(int(letter_in_ord))
    deciher_word.append(letter_in_ord)

    for letter in current_word:
        if not letter.isdigit():
            deciher_word.append(letter)

    result.append("".join(swap(deciher_word)))


print(" ".join(result))