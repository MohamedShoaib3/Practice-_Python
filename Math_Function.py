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

# Function to find the floor value of a number
def floor(number):
    if number >= 0:
        return int(number)  # Return the integer part directly for non-negative numbers
    else:
        int_part = int(number)  # Get the integer part of the negative number
        return int_part if int_part == number else int_part - 1  # Adjust if it's not an integer

# Function to find the ceiling value of a number
def mceil(number):
    if number < 0:
        return int(number)  # Return the integer part directly for negative numbers
    else:
        int_part = int(number)  # Get the integer part of the non-negative number
        return int_part if int_part == number else int_part + 1  # Adjust if it's not an integer

# Function to calculate the factorial of a number
def factorial(num): 
    if num < 0:
        print("Factorial is not defined for negative values")
        return None  # Return None for negative input
    elif num == 0 or num == 1:
        return 1  # The factorial of 0 or 1 is 1
    else:
        ans = 1  # Initialize the answer to 1
        for i in range(1, num + 1):
            ans *= i  # Multiply ans by i in each iteration
        return ans  # Return the calculated factorial

# Function to calculate the power of num1 raised to num2
def pow(num1, num2):
    power = num1 ** num2  # Raise num1 to the power of num2
    return power  # Return the result

# Function to return the value of pi (π)
def pi():
    return 3.141592653589793  # Return the mathematical constant pi

# Function to return the value of e (Euler's number)
def e():
    return 2.718281828459045  # Return the mathematical constant e

# Function to convert radians to degrees
def degrees(num):
    deg = num * (180 / pi())  # Convert radians to degrees
    return deg  # Return the result in degrees

# Function to convert degrees to radians
def radians(num):
    rad = num * (pi() / 180)  # Convert degrees to radians
    return rad  # Return the result in radians

# Function to calculate the exponential of a number
def exp(num):
    ans = e() ** num  # Raise e to the power of num
    return ans  # Return the result





