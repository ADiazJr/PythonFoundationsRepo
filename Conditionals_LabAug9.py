legal_driving_age = 16
user_age = float(input('Please type your age:'))
if user_age >= legal_driving_age:
    print('You are legally able to drive')
elif user_age <= legal_driving_age:
    print('You are not old enough to drive yet')

import random
Random_to_ten = random.randrange(10)

if Random_to_ten <= 2:
    print('0 or 1 or 2')
elif Random_to_ten <= 5:
    print('3 or 4 or 5')
elif Random_to_ten <= 8:
    print('6 or 7 or 8')
elif Random_to_ten <= 10:
    print('9 or 10')

NFL_team_name = input('Please type your favorite NFL team:')

if NFL_team_name == "Bears":
    print('Quarterback Much?')
elif NFL_team_name == "Vikings":
    print('Loud noises!')
elif NFL_team_name == "Lions":
    print('LOL! They bad!')
elif NFL_team_name == "Packers":
    print('Best team in the world! Actually in the universe')
else:
    input("Pick a different team:")