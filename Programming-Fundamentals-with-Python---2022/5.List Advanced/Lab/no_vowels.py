
# 'a', 'o', 'u', 'e', 'i'.


text = input()
vowels = ['a', 'o', 'u', 'e', 'i']

non_vocals = [el for el in text if el.lower() not in vowels]

print("".join(non_vocals))