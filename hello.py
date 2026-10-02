# Ask user for their name
name = input ("What is your name? ").strip().title()

# Remove whitespace from str
#name = name.strip().title()

# Capitalize user's name
#name = name.capitalize()

# Capitalize the first letter of each word in the user's name
#name = name.title()

# Splits users name into first name and last name
first, last = name.split(" ")

#Say hello to the user
print(f"Hello, {first}! Today begins my journey.")