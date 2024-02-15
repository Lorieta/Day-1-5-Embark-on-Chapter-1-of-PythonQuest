# Write the code ↓ to read the user's input for a non-negative integer.
# Be cautious when reading input of various data types.
print("FACTORIAL CALCULATOR FOR ALF")
result = 1
factorial = int(input("Please, enter a non-negative integer:  "))

# Write the code ↓ to calculate the factorial of the user-defined integer using a loop.
for i in range(factorial):
    result *= i + 1

# Write the code ↓ to display the factorial result.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("The factorial of" + f" {factorial} " + f" is {result}")
