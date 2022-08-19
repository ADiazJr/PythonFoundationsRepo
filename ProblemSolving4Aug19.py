# #Task 1
# def task1():
#     some_list = [5, 17, 77 , 50]
#     if index_target_finder(some_list, 55) is True:
#         print("there is a match")
#     else:
#         print("no match was found")
    

# def index_target_finder(list, target_number):
#     list_og = len(list)
#     for item in range(len(list)):
#         for item2 in range(len(list)):
#             sum = 0
#             sum = list[item] +list[item2+1]
#             list.append(sum)
#             if target_number in list:
#                 return True
#             elif (item2 +1) == list_og:
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
def task3(example_list):
    example_list.sort()
    for number in range(len(example_list)):
        if example_list[number+1] != (example_list[number]+1):
            return False
        else:
            return True

some_list1 = [5,7,3,4,6]
print(task3(some_list1))