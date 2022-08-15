favorite_number = 7
import random

random_number = random.randrange(15)
print(random_number)
numbers_away_from_favorite = random_number - favorite_number
print(abs(numbers_away_from_favorite))