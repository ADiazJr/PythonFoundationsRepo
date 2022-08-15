# #Task 1
# program_languages = ['JavaScript', 'Python', "Java", "Django", "React" ]
# print(program_languages[1])

# #Task 2
# instructors = ['Nevin', 'Mike', 'Jake', 'Dan', 'Megan']
# instructors.append('Dan')
# instructors.append('James')
# instructors.append('John-Boy')
# instructors[3] = 'Danimal'
# print(instructors)

# #Task 3
# John_leaving = instructors.pop(7)
# print(instructors)

# #Task 4
# mike_leaving = instructors.remove("Mike")
# print(instructors)

# #Task 5
# first_word = ['fan', 'bull-', 'barrel-o', 'slap']
# second_word = ['dango', 'rider', 'monkeys', 'stick']

# for word in range(len(first_word)):
#     print(first_word[word] + second_word[word])

# #Task 6
# New_Name = input('Type in Instructors name:')
# is_a_duplicate = False
# for name in range(len(instructors)):
#     if instructors[name] == New_Name:
#         print('Sorry that name has been taken, please provide a nickname')
#         is_a_duplicate = True

# while is_a_duplicate is False:
#     instructors.append(New_Name)
#     print(instructors)
#     is_a_duplicate = True


# #Task 7
# fav_places = ['Germany', 'Japan']
# More_places = ['Italy', 'Brazil', 'Spain']
# all_places = fav_places + More_places
# print(all_places)
# for places in More_places:
#     fav_places.append(places)
# print(fav_places)   
# fav_places.extend(More_places)
# print(fav_places)

# #Task 8
# favorite_cars = ['Tesla', 'Ferrari', 'Lambhorgini']
# cool_cars = favorite_cars.copy()
# print(cool_cars)
# cooler_cars = list(favorite_cars)
# print(cooler_cars)
# coolest_cars = []
# for cars in favorite_cars:
#     coolest_cars.append(cars)
# print(coolest_cars)

#Task 9
# favorite_food = ["shrimp scampi", "tenders", "chicken aflredo", "shrimp fried rice", "lobster roll"]
# favorite_food.sort()
# print(favorite_food)
# favorite_food.sort(reverse=True)
# print(favorite_food)
# for index_one in range(len(favorite_food)):
#     for index_two in range(index_one+1,len(favorite_food)):
#         if favorite_food[index_one]>favorite_food[index_two]:
#             favorite_food[index_one],favorite_food[index_two] = favorite_food[index_two],favorite_food[index_one]
# print(favorite_food)
# print("a"<"b") python can compare strings alphanumerically
