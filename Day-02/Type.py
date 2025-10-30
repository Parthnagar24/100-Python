# Type Checking in Python
print(type("hello"))     # <class 'str'>
print(type(123))         # <class 'int'>
print(type(45.67))       # <class 'float'>
print(type([1, 2, 3]))   # <class 'list'>
print(type((1, 2, 3)))   # <class 'tuple'>
print(type({1, 2, 3}))   # <class 'set'>
print(type(True))        # <class 'bool'>

# Type Conversion in Python (changing one data type to another)
print("123" + "563")             # String concatenation -> Output: 123563
print(int("123") + int("563"))   # Integer addition -> Output: 686

# Common type conversion functions
int()    # Converts to integer
float()  # Converts to floating-point number
str()    # Converts to string
bool()   # Converts to boolean

# Example: Using type conversion with len() and str()
print("Number of letters in your name: " + str(len(input("Enter your name: "))))
