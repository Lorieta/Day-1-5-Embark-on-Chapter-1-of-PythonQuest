# Write the code ↓ to read the user's input for a positive integer.
# Be cautious when reading input of various data types.
print("PERFECT NUMBER DETERMINATOR")
num = int(input("Please,enter number a positive integer: "))
sum = 0
# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    result = "a Perfect number."
else:
    result = "not a perfect Number."

# Write the code ↓ to display the Perfect Number check result.
# NOTE : You can use if-else statement or ternary operator to display the result.
print(f"{num}", f"is {result}")
