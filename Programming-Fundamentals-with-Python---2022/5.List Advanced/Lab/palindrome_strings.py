# On the first line, you will receive words separated by a single space.
# On the second line, you will receive a palindrome.
# First, you should print a list containing all the found palindromes in the sequence.
# Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".



words = [word for word in input().split() if word == word[::-1]]
palindrome = input()

print(words)
counter = words.count(palindrome)
print(f"Found palindrome {counter} times")