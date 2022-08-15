def happy_number_check(possible_happy_number):
    number_check = False
    squared_value = square(possible_happy_number)
    while number_check is False:
        if squared_value == 1:
            print("Number is happy")
            number_check = True
        elif squared_value !=1:
            squared_value = square(squared_value)
def square(number_to_square):
    checked_number = 0
    for number in str(number_to_square):
        number_squared = int(number)*int(number) 
        checked_number += number_squared
    return checked_number


    
happy_number_check(13)