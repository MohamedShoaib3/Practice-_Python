# Function to convert all lowercase letters in the string to uppercase
def upper(world):
    result = ""  # Initialize an empty string to store the result
    for i in world:
        # Check if the character is lowercase (ASCII range 97 to 122)
        if ord(i) >= 97 and ord(i) <= 122:
            # Convert to uppercase by subtracting 32 from the ASCII code
            result += chr(ord(i) - 32)
        else:
            # If it's not lowercase, keep the character as is
            result += i
    return result  # Return the resulting uppercase string

# Function to convert all uppercase letters in the string to lowercase
def lower(world):
    result = ""  # Initialize an empty string to store the result
    for i in world:
        # Check if the character is uppercase (ASCII range 65 to 90)
        if ord(i) >= 65 and ord(i) <= 90:
            # Convert to lowercase by adding 32 to the ASCII code
            result += chr(ord(i) + 32)
        else:
            # If it's not uppercase, keep the character as is
            result += i
    return result  # Return the resulting lowercase string

# Function to capitalize the first letter of the string
def capitalize(world):
    # Check if the first character is lowercase
    if len(world) > 0 and ord(world[0]) >= 97 and ord(world[0]) <= 122:
        # Capitalize the first letter by subtracting 32 from its ASCII code
        world = chr(ord(world[0]) - 32) + world[1:]  # Replace the first character
    return world  # Return the modified string

# Function to count the occurrences of a substring in the string
def count(world, substring):
    count = 0  # Initialize a counter to zero
    for i in world:
        # Check if the current character matches the substring
        if i == substring:
            count += 1  # Increment the count if a match is found
    return count  # Return the total count of occurrences

# Function to check if the string consists only of numeric characters
def isnumeric(world):
    ans = True  # Assume the string is numeric initially
    for i in world:
        # Check if the character is a digit (ASCII range 48 to 57)
        if ord(i) > 48 and ord(i) < 57:
            ans = True  # Set ans to False if a non-numeric character is found
            break  # Exit the loop early
    return ans  # Return whether the string is numeric

# Function to check if the string is alphanumeric (contains letters or numbers)
def isalnum(world):
    ans = True  # Assume the string is alphanumeric initially
    for i in world:
        # Check if the character is a digit (ASCII range 48 to 57)
        if ord(i) >= 48 and ord(i) <= 57:
            continue  # Continue if it's a digit
        # Check if the character is a lowercase letter (ASCII range 97 to 122)
        elif ord(i) >= 97 and ord(i) <= 122:
            continue  # Continue if it's a lowercase letter
        # Check if the character is an uppercase letter (ASCII range 65 to 90)
        elif ord(i) >= 65 and ord(i) <= 90:
            continue  # Continue if it's an uppercase letter
        else:
            ans = False  # Set ans to False if a non-alphanumeric character is found
            break  # Exit the loop early
    return ans  # Return whether the string is alphanumeric

# Function to check if all characters in the string are uppercase
def isupper(world):
    ans = True  # Assume the string is uppercase initially
    for i in world:
        # Check if the character is a lowercase letter (ASCII range 97 to 122)
        if ord(i) >= 97 and ord(i) <= 122:
            ans = False  # Set ans to False if a lowercase letter is found
            break  # Exit the loop early
    return ans  # Return whether the string is uppercase

# Function to check if all characters in the string are lowercase
def islower(world):
    ans = True  # Assume the string is lowercase initially
    for i in world:
        # Check if the character is an uppercase letter (ASCII range 65 to 90)
        if ord(i) >= 65 and ord(i) <= 90:
            ans = False  # Set ans to False if an uppercase letter is found
            break  # Exit the loop early
    return ans  # Return whether the string is lowercase

