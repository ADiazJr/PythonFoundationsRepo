# # #Task 1
# def shorten(string_one):
#     for character in range(len(string_one)):
#         if character == 0:
#             shortened_version = ''
#             shortened_version += string_one[character]
#         if (len(string_one) - character) == 1:
#             shortened_version += string_one[character]
#     print(shortened_version)
#     return

# shorten("Rocky")

# #Task 2
# def pBJ():
#     for number in range(101):
#         if (number % 5) + (number % 3) == 0:
#             print('peanut butter jelly')
#         elif (number % 5) == 0:
#             print('jelly')                                                 
#         elif (number % 3) == 0:
#             print('peanut butter')
#         else:
#             print(number)

# pBJ()

# #Task 3
# def WLIndexing(string_two):
#     final_result = " "
#     for character_one in string_two:
#         for character_two in range(len(string_two)):
#             if len(string_two) >= character_two +1:
#                 final_result += character_one
#                 final_result += str(character_two)
#                 character_one = str(string_two[character_two +1])
#         print(final_result)
#         break
#     return WLIndexing

# def WLIndexing(string_two):
#     final_result = " "
#     for index in range(len(string_two)):
#         final_result += string_two[index]
#         final_result += str(index)
#     print(final_result)

# WLIndexing("World Peace")

#Task 4
def ingr_search(ingredients):
    user_input = input("What ingredient are you searching for:")
    ingredient_match = True
    while ingredient_match is True:
        for ingredient in ingredients:
            if ingredient == user_input:
                print(f'There was a match with {ingredient}')
                ingredient_match = False
                return ingredient
            if ingredient != user_input and ingredients[-1] == ingredient:
                user_input = input("would you like to search again? Please Type New Ingredient:")
        

ingr_search(['carrot', 'tomato', 'onion'])

#Task 5
# def reverse(list_one):
#     list_reversed = " "
#     for item in range(len(list_one)-1, -1, -1):
#         list_reversed += list_one[item] + ", "
        
#     return list_reversed

# list_i_want = reverse(['Yellow', 'purple', 'Orange'])
# print(list_i_want)

#Task 6
# def drop_four(names):
#     long_names = " "
#     for name in names: 
#         if len(name) >= 5:
#             long_names += name +", "
#     return long_names

# list_of_long_names = drop_four(["Rocky", 'Miriam', "Irene", "bob", "gil"])
# print(list_of_long_names)

