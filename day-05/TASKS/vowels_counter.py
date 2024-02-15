# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.
print("VOWEL COUNTER FOR ALF")
count = 0
word = input("Please, enter a word/s to check:")
vowels = "aeiouAEIOU"


# Write the code ↓ to count the number of vowels in the entered word.
# Utilize string functions to iterate through the characters and identify vowels.
for char in word:
    if char in vowels:
        count += 1

# Write the code ↓ to display the count of vowels in the word.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print(f"The number of vowels in the '{word}' is: {count} ")
