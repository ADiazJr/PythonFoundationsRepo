my_current_age_2022 = 22
print(f'I am {my_current_age_2022} years old')
my_first_name = input('Please type your first name:')
my_last_name = input('Please type your last name:')
my_full_name = my_first_name + " " + my_last_name
print(f'My first name is {my_first_name} and my last name is {my_last_name}, which means my full name is {my_full_name}')

current_fahrenheit_temperature = input('Type in Fahrenheit temperature:')
current_fahrenheit_temperature_converted = float(current_fahrenheit_temperature)
current_celsius_temperature = (current_fahrenheit_temperature_converted - 32) * 0.5556
print(f'{current_fahrenheit_temperature} degrees Fahrenheit is {current_celsius_temperature} degrees Celsius')