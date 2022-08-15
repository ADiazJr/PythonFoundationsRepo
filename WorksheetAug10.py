#Task 1
greeting = 'hello'
reverse_greeting = ''
for index_number in range(len(greeting) - 1, -1, -1):
    reverse_greeting = (greeting[index_number]) + (greeting[index_number -1]) +(greeting[index_number -2]) + (greeting[index_number -3]) + (greeting[index_number -4])
    break
print(reverse_greeting)

word = "Hello"
final_word = ""
for index_number in range(len(word) - 1, -1, -1):
    final_word += word[index_number]

print(final_word)

#Task 2
original_input = input("what you want capitalized:")
captialized_input = ''

for character in range(len(original_input)):
    if character == 0:
        first_letter = original_input[character]
        first_letter = first_letter.upper()
        captialized_input += first_letter
        continue
    if original_input[character - 1] == ' ':
        uppercase_letter = original_input[character]
        uppercase_letter = uppercase_letter.upper()
        captialized_input += uppercase_letter
        continue
    captialized_input += original_input[character]

print(captialized_input)

#Task 3
possible_palindrome = input("Please Enter Possible Palindrome:")
Palindrome = ""

for character in range(len(possible_palindrome) -1, -1 ,-1):
    Palindrome += possible_palindrome[character]
    palindrome_match = False
while palindrome_match == False:
    if Palindrome == possible_palindrome:
        print(f'There was a Palindrome Match with {Palindrome}')
        palindrome_match = True
    else:
        print('This word is not a Palindrome')
        palindrome_match = True

#Task 4
input_to_compress = input('PLease type something to compress:')
compressed_input = ""
string_match_number = 1
for uncompressed_character in range(len(input_to_compress)):
    if (uncompressed_character) >= (len(input_to_compress)-1):
        compressed_input += str(string_match_number)
        compressed_input += input_to_compress[uncompressed_character]
        print(compressed_input)
    elif input_to_compress[uncompressed_character] == input_to_compress[uncompressed_character +1]:
        string_match_number += 1
    else:
        compressed_input += str(string_match_number)
        compressed_input += input_to_compress[uncompressed_character]
        string_match_number = 1

