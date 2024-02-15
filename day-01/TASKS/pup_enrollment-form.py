# Write the code ↓ to read user's input.
# Be cautious when reading input of various data types.
print("PUP Enrollment Form\n")
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
prevGWA = float(input("Enter your previous general weighted average:"))
isMember = bool(
    input("Are you a member of AWS Cloud Club? (yes/no): \n").lower() == "yes"
)


# Write the code ↓ to display the user's personal information.
print("Your Enrollment Form\n")
print(
    f"Name: {name} "
    + "\n"
    + f"Age: {age}"
    + "\n"
    + f"GWA: {prevGWA:.2f} "
    + "\n"
    + f"Awstraunot: {isMember} ",
)
# Select and employ a string concatenation method based on your personal preference and comfort level.
