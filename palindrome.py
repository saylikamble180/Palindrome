# Palindrome of a string

n = input()
rev=""
for char in n:
    rev = char + rev
if n == rev:
    print("Yes, The string is palindrome")
else:
    print("No, The string is not palindrome")