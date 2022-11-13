str_for_remove = input()
text = input()


while str_for_remove in text:
    text = text.replace(str_for_remove, "")
print(text)