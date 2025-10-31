# 05-Escaping_A_String

# In Python, certain characters have special meanings in strings.
# For example, the double quote (") is used to start and end a string.
# If you want to include a double quote *inside* a string that’s also enclosed in double quotes,
# you must escape it using a backslash (\).

# Example 1: Escaping double quotes
speech = "She said: \"Hi\""
print(speech)
# Output: She said: "Hi"

# Example 2: Escaping single quotes inside a single-quoted string
sentence = 'It\'s a beautiful day'
print(sentence)
# Output: It's a beautiful day

# Example 3: Escaping backslash itself
path = "C:\\Users\\Parth"
print(path)
# Output: C:\Users\Parth

# Example 4: Newline and tab escape characters
message = "Hello,\nWelcome to Python!\tLet's learn."
print(message)
# Output:
# Hello,
# Welcome to Python!	Let's learn.
# (\n adds a new line, \t adds a tab space)

# Example 5: Using raw strings to avoid escaping (prefix with r)
raw_path = r"C:\Users\Parth"
print(raw_path)
# Output: C:\Users\Parth
# (The 'r' tells Python to treat backslashes literally — no escaping)
