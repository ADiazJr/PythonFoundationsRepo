import re
#Task 1

def task1():
    some_list = [5, 17, 77 , 50]
    if index_target_finder(some_list, 55) is True:
        print("there is a match")
    else:
        print("no match was found")
    

def index_target_finder(list, target_number):
    list_og = len(list)
    for index in range(len(list)):
        for index2 in range(len(list)):
            sum = 0
            sum = list[index] +list[index2+1]
            list.append(sum)
            if target_number in list:
                return True
            elif (index2 +1) == list_og:
                return False

task1()

#Task 2
def palindrome_check(possible_palindrome):
    Palindrome = ""
    for character in range(len(possible_palindrome) -1, -1 ,-1):
        Palindrome += possible_palindrome[character]
        palindrome_match = False
    while palindrome_match == False:
        if Palindrome == possible_palindrome:
            print('Palindrome Match is True')
            palindrome_match = True
        else:
            print('Palindrome Match is False')
            palindrome_match = True
palindrome_check(input("Please Enter Possible Palindrome:"))

#Task 3
def task3(example_list):
    example_list.sort()
    for index in range(len(example_list)):
        if example_list[index+1] != (example_list[index]+1):
            return False
        else:
            return True

some_list1 = [5,7,3,4,6]
print(task3(some_list1))

#Task 4
def sum_of_arrays(array):
    negative_sum = 0
    positive_sum = 0
    for number in array:
        if number <= -1:
            negative_sum = negative_sum + number
        elif number >= 0:
            positive_sum = positive_sum + number
    return [positive_sum,negative_sum]

use_case_array = [7,9,-3,-32,107,-1,36,95,-14,-99,21]
print(sum_of_arrays(use_case_array))

#Task 5
def high_and_low(number_string_seperated):
    list_of_numbers = []
    ended_string = False
    while ended_string is False:
       for index in range(len(number_string_seperated)):
            if (index +1) >= len(number_string_seperated):
                list_of_numbers.append(int(number_string_seperated[index]))
                ended_string = True
            elif number_string_seperated[index +1] != " " and number_string_seperated[index] !=" ":
                double_digit = ''
                double_digit += number_string_seperated[index]
            elif number_string_seperated[index -1] != " " and number_string_seperated[index] !=" " and index != 0:
                double_digit += number_string_seperated[index]
                list_of_numbers.append(int(double_digit))
            elif number_string_seperated[index] != ' ':
                list_of_numbers.append(int(number_string_seperated[index]))
    list_of_numbers.sort()
    return [list_of_numbers[0],list_of_numbers[-1]]

use_case_string = "3 9 0 1 4 8 10 2"
print(high_and_low(use_case_string))

#Task 6 

def email_validation(email):
    if comcheck(email):
        if atcheck(email):
            if kinds(email):
                print('Email validated')
            else:
                print('Email not validated')
        else:
            print('Email not validated')
    else:
        print('Email not validated')        
      
def kinds(email):
    validation = re.search('gmail|yahoo|outlook|hotmail', email)
    if validation.string:
        return True
    else:
        return False
def atcheck(email):
    validation = re.search('@', email)
    if validation:
        return True
    else:
        return False
def comcheck(email):
    validation = re.search(".com$", email)
    if validation.string:
        return True
    else:
        return False


email = 'arturodiaz@gmail.com'
email_validation(email)

#Task 7
# numericlist = "abcdefghijklmnopqrstubwxyz"
# for number in range(0, 25):
#     for character in numericlist:
#         "abcdefghijklmnopqrstubwxyz"
# print(numericlist)

numericlist = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

# print(ord('r'))