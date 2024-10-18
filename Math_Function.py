# Function to find the minimum value between two numbers
def min(num1, num2):
    if num1 > num2:
        print(num2)  # If num1 is greater, print num2
    else:
        print(num1)  # Otherwise, print num1

# Function to find the maximum value between two numbers
def max(num1, num2):
    if num1 > num2:
        print(num1)  # If num1 is greater, print num1
    else:
        print(num2)  # Otherwise, print num2

# Function to get the absolute value of a number
def absolute(num):
    if num < 0:
        return -num  # If the number is negative, return its positive value
    return num  # Otherwise, return the number as is

# Function to find the maximum value between two numbers after converting them to absolute values
def max_absolute(num1, num2):
    num1 = absolute(num1)  # Convert num1 to its absolute value
    num2 = absolute(num2)  # Convert num2 to its absolute value
    if num1 > num2:
        return num1  # If the absolute value of num1 is greater, return num1
    else:
        return num2  # Otherwise, return num2
