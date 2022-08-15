for number in range(5):
    print('Hello!')

for number in range(11):
    print(number) 

for number in range(10, 0, -1):
    print(number)

user_input = input('Please type number of times you want to see devCodeCamp:')
user_input_converted = int(user_input)
for number in range(user_input_converted):
    print('devCodeCamp') 

cheese_heads = "packers"
for number in cheese_heads:
    print(number)

for number in range(101):
    if (number % 5) + (number % 3) == 0:
        print('fizzbuzz')
    elif (number % 5) == 0:
        print('buzz')                                                 
    elif (number % 3) == 0:
        print('fizz')
    else:
        print(number)

Number_of_hello = 0
stop_saying_hello = True
while stop_saying_hello is True:
    if Number_of_hello >= 5:
        stop_saying_hello =  False
    else:
        Number_of_hello += 1
        print('hello!')

password_key = "password"
User_access = True
while User_access is True:
    if input("Please Type Password:") == password_key:
        User_access = False
        print("User Validated")
