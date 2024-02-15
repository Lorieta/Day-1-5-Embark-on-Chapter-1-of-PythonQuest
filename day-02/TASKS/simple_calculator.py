# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.
fnum = float(input("Enter the first number: "))
snum = float(input("Enter the second number: "))
operator = input("Enter the operator (+,-,x,/): ")

# Write the code ↓ to perform the calculations based on the selected operation.
if operator == "+":
    result = fnum + snum

elif operator == "-":
    result = fnum - snum

elif operator == "x":
    result = fnum * snum

elif operator == "/":
    result = fnum / snum

else:
    print("Invalid")

# Write the code ↓ to display the result.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("The result of" + f" {fnum} " + f" {operator} " + f" {snum} " + f"is {result} ")
