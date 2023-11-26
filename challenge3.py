def solve(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    max_value = 0
    current_value = 0
    
    for char in s:
        if char in consonants:
            current_value += ord(char) - ord('a') + 1
        else:
            max_value = max(max_value, current_value)
            current_value = 0
    
    max_value = max(max_value, current_value)
    return max_value

# Ask the user for input
word = input("Enter a word (lowercase and alphabetic characters only): ")

# Call the function with user input
result = solve(word)

# Display the result
print("The highest value of consonant substrings:", result)
