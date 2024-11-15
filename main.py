# Joshua
# 11/13/24
# Practice: Positional & Keyword Arguments in Python


# POSITIONAL ARGUMENTS
# Start by writing the code to create the three functions outlined below
# You'll use only positional arguments in the first three functions
# Test your code and correct any errors

# Greet The User
# Write a function that takes two parameters -- first name and age
# Use an f-string to welcome the user by first name and to display his/her age
# def welcome_user(first_name, age):
#     print(f'Hello, {first_name}. You are {age} years old.')

# JUST A TEST-->
# firstname = input("Please enter your first name")
# firstname = firstname.capitalize
# yrs_old = int(input('Please enter your age'))

# welcome_user('Joshua', 18)

# Area of a Rectangle
# Write a function to calculate the area (in square feet) of a rectangle
# Your two parameters will be length and width
# The print statement in the function should display the length, width and area (in square feet) of your rectangle
# def area_of_rect(length, width):
#     area = length * width
#     print(F'The rounded area of the rectangle is {area}')

# area_of_rect(13, 27)

# Sum of Numbers
# Write a function that finds the sum of three numbers
# Your three parameters will be num1, num2, and num3
# The print statement in the function should display the sum of the three numbers
# def sum_of_number(num1, num2, num3):
#     sum = num1 + num2 + num3
#     print(f'The sum of the three numbers is {sum}.')

# sum_of_number(2, 2, 87)

# KEYWORD ARGUMENTS
# Create the three functions outlined below
# In these last three functions, you'll use only keyword arguments 
# Test your code and correct any errors

# Greet By Title
# Write a function that greets the user by title, first name and last name
# Examples of titles include: Mr., Ms., Mrs. and Dr.
# When calling your function, change the order of your keyword arguments so that they don't match the order of your function parameters

# def greet_by_title(title, first_name, last_name):
#     # title = title.capitalize
#     # first_name = first_name.capitalize
#     # last_name = last_name.capitalize
#     print(f'Hello {first_name} {last_name}, the {title}')

# greet_by_title (last_name = 'Phillips', first_name = 'Joshua', title = 'Youtuber')

# Describe Your Pet
# Write a function that says what type of pet you have and what your pet's name is
# Your function parameters will be pet_type and pet_name

# def desc_your_pet(pet_type, pet_name):
#     print(f'My {pet_type} is named, {pet_name}.')

# desc_your_pet(pet_name = 'Sherbert', pet_type = 'Cat')

# Updated Function
# Choose any ONE of the first three functions from this project and rewrite it below using keyword arguments

def area_of_rect(width, length):
    area = length * width
    print(f'The rounded area of the rectangle is {area}')

area_of_rect(length=32, width=40)