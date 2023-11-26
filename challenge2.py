def check_positive_negative(a, b, c):
    positive_count = 0
    negative_count = 0

    if a > 0:
        positive_count += 1
    elif a < 0:
        negative_count += 1

    if b > 0:
        positive_count += 1
    elif b < 0:
        negative_count += 1

    if c > 0:
        positive_count += 1
    elif c < 0:
        negative_count += 1

    return positive_count == 2 and negative_count == 1

# Ask the user for input
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

# Call the function with user input
result = check_positive_negative(a, b, c)

# Display the result
if result:
    print("True.")
else:
    print("False.")
