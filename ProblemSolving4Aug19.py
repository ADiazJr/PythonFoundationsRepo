# #Task 1
# def task1():
#     some_list = [5, 17, 77 , 50]
#     if index_target_finder(some_list, 55) is True:
#         print("there is a match")
#     else:
#         print("no match was found")
    

# def index_target_finder(list, target_number):
#     list_og = len(list)
#     for index in range(len(list)):
#         for index2 in range(len(list)):
#             sum = 0
#             sum = list[index] +list[index2+1]
#             list.append(sum)
#             if target_number in list:
#                 return True
#             elif (index2 +1) == list_og:
#                 return False

# task1()

# #Task 2
# def palindrome_check(possible_palindrome):
#     Palindrome = ""
#     for character in range(len(possible_palindrome) -1, -1 ,-1):
#         Palindrome += possible_palindrome[character]
#         palindrome_match = False
#     while palindrome_match == False:
#         if Palindrome == possible_palindrome:
#             print('Palindrome Match is True')
#             palindrome_match = True
#         else:
#             print('Palindrome Match is False')
#             palindrome_match = True
# palindrome_check(input("Please Enter Possible Palindrome:"))

#Task 3
# def task3(example_list):
#     example_list.sort()
#     for index in range(len(example_list)):
#         if example_list[index+1] != (example_list[index]+1):
#             return False
#         else:
#             return True

# some_list1 = [5,7,3,4,6]
# print(task3(some_list1))

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