def happy_number_check(possible_happy_number):
    number_check = False
    squared_value = square(possible_happy_number)
    list_of_squared_value = [0]
    while number_check is False:
        if squared_value == 1:
            print("Number is happy")
            number_check = True
        elif squared_value !=1:
            return_of_list = place_squared_value_in_list(squared_value,list_of_squared_value)
            squared_value = square(squared_value)
            if check_value(return_of_list, squared_value) == True:
                print('this is a sad number')
                number_check = False
                return
            
def square(number_to_square):
    checked_number = 0
    for number in str(number_to_square):
        number_squared = int(number)*int(number) 
        checked_number += number_squared
    return checked_number
def place_squared_value_in_list(squared_value,list_of_squared_value):
    list_of_squared_value.append(squared_value)
    return list_of_squared_value
def check_value(return_of_list, squared_value):
    for value in range(len(return_of_list)):
        if squared_value == return_of_list[value]:
            return True
        elif value == len(return_of_list)-1:
            return False

happy_number_check(input('Please Type to Check If Number Is Happy or Sad:'))

def check_prime(user_input):
    if user_input == 3 or user_input == 2 or (user_input % 2 != 0 and user_input % 3 != 0):
        print("Number is Prime")
        return
    elif user_input % 2 == 0 or user_input % 3 == 0:
        print("number is composite")

check_prime(int(input("Please type number to check if it's prime:")))

def fibonacci():
    fibonacci_sequence = [1,1]
    never = False
    while never is False:
        for number in range(100):
            number_after_addition = fibonacci_sequence[number +1] + (fibonacci_sequence[number])
            fibonacci_sequence.append(number_after_addition)
fibonacci()

def fibonacci_input(user_input):
    fibonacci_sequence = [user_input,user_input]
    never = False
    while never is False:
        for number in range(100):
            number_after_addition = fibonacci_sequence[number +1] + (fibonacci_sequence[number])
            fibonacci_sequence.append(number_after_addition)
fibonacci_input(int(input("Type number to start Fibonacci Sequence:")))