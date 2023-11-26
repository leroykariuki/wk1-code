def convert_to_24_hour(hour, minute, period):
    if period == "pm" and hour != 12:
        hour = (hour + 12) % 24
    elif period == "am" and hour == 12:
        hour = 0
    
    return "{:02d}{:02d}".format(hour, minute)

# Ask the user for input
time_input = input("Enter the time in 12-hour format (e.g., 9:30 pm): ")
hour, minute_period = time_input.split(":")
minute, period = minute_period.split()

# Convert strings to integers
hour = int(hour)
minute = int(minute)

# Call the function with user input
result = convert_to_24_hour(hour, minute, period)
print("Converted 24-hour time:", result)
