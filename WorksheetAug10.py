# greeting = 'hello'
# reverse_greeting = ''
# for index_number in range(len(greeting) - 1, -1, -1):
#     reverse_greeting = (greeting[index_number]) + (greeting[index_number -1]) +(greeting[index_number -2]) + (greeting[index_number -3]) + (greeting[index_number -4])
#     break
# print(reverse_greeting)

word = "Hello"
final_word = ""
for index_number in range(len(word) - 1, -1, -1):
    final_word += word[index_number]

print(final_word)

# original_input = input("what you want capitalized:")
# captialized_input = ''

# for character in range(len(original_input)):
#     if character == 0:
#         first_letter = original_input[character]
#         first_letter = first_letter.upper()
#         captialized_input += first_letter
#         continue
#     if original_input[character - 1] == ' ':
#         uppercase_letter = original_input[character]
#         uppercase_letter = uppercase_letter.upper()
#         captialized_input += uppercase_letter
#         continue
#     captialized_input += original_input[character]

# print(captialized_input)

# possible_palindrome = input("Do not type a Palindrome")
# Palindrome = ""

# for character in range(len(possible_palindrome))

