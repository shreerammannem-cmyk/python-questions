# 1. Check if all characters in the string are digits
x = "123"
y = "abc123"

print(x.isdigit())  # Output: True
print(y.isdigit())  # Output: False

# 2. Check if all characters in the string are alphabets
a = "abc"
b = "123abc"

print(a.isalpha())  # Output: True
print(b.isalpha())  # Output: False

# 3. Check if all characters are alphanumeric (letters or numbers only)
m = "abc123"
n = "ab@*#123"

print(m.isalnum())  # Output: True
print(n.isalnum())  # Output: False (contains special characters @, *, #)