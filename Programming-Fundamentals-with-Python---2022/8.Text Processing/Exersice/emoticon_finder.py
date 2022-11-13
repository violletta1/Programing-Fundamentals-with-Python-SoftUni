# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.
# Input: There are so many emoticons nowadays :P. I have many ideas :O what input to place here
# Output # :)
         # :P
         #:O
         # :)

text = input()

for index in range(len(text)):
    if text[index] == ":":
        print(text[index] + text[index + 1])