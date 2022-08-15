# Example function:
import string


def display_name(name):
    print(name)
    #  this is the logic of the function

# The above function takes in a variable, known as the parameter.
# In this example, that variable is name.
# The function then prints to the console the value that is passed in


display_name('Mike')
display_name('Ian')
display_name('Nevin')

# Above we are now calling the function. This means using the function that we wrote.
# Here we are passing in an actual value. In this case, the value is 'Mike'

# Example 2


def add_one_to_number(number):
    number_one = 1
    add_one = number + number_one
    return add_one

# The above function takes in a variable, known as the parameter.
# In this example, that variable is number.
# The function then adds one to the parameter and returns the sum


result = add_one_to_number(30)

# Above we are now calling the function. This means using the function that we wrote.
# Here we are passing in an actual value. In this case, the value is 30
# We create and set a variable equal to the function call becuase the function returns a value

# Problem 1
# Write a function that takes in two numbers
# The logic of the function should add those two numbers together and return a sum
# Capture the returned value in a variable and print it to the console
def sum_of_numbers(first_number, second_number):
    result_of_sum = first_number + second_number
    return result_of_sum

result_one = sum_of_numbers(2, 3)
print(result_one)
# Problem 2
# Write a function that takes in two strings
# The logic of the function should concatenate those two strings together and return the concatenated result
# Capture the returned value in a variable and print it to the console
def concatenate(string_one, string_two):
    concatenation_of_strings = string_one + string_two
    return concatenation_of_strings

concatenation_result = concatenate("Spider", "-Man")
print(concatenation_result)

# Problem 3
# Write a function that takes in a string
# The logic of the function should print each character of the string one at a time to the console
# HINT: for loop is one way to do this
def acronronymize(string_problem_three):
    for character in string_problem_three:
        print(character)
    return
acronronymize("pancakes")

# Problem 4
# Write a function that takes in a string
# The logic of the function should print the string to the console but only if that string has three or more characters in it
# If it is less than three characters, then print to the console 'we need a larger string to print!'
def string_size_check(string_four):
    if len(string_four) >= 3:
        print(string_four)
    elif len(string_four) <=2:
        print("we need a larger string to print!")
    return
string_size_check("on")
