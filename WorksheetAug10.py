#Task 1
def reverse(greeting):
    final_word = ""
    for index_number in range(len(greeting) - 1, -1, -1):
        final_word += greeting[index_number]
    return final_word

hello_backwards = reverse("Hello")
print(hello_backwards)

# #Task 2
def capitalize(original_input):
    capped_input = ''
    for character in range(len(original_input)):
        if character == 0:
            first_letter = original_input[character]
            first_letter = first_letter.upper()
            capped_input += first_letter
            continue
        if original_input[character - 1] == ' ':
            uppercase_letter = original_input[character]
            uppercase_letter = uppercase_letter.upper()
            capped_input += uppercase_letter
            continue
        capped_input += original_input[character]
    return capped_input

print_capped_input = capitalize(input("what you want capitalized:"))
print(print_capped_input)

# #Task 3
def palindrome_check(possible_palindrome):
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
palindrome_check(input("Please Enter Possible Palindrome:"))

# #Task 4
def compress(input_to_compress):
    compressed_input = ""
    string_match_number = 1
    for uncompressed_character in range(len(input_to_compress)):
        if (uncompressed_character) >= (len(input_to_compress)-1):
            compressed_input += str(string_match_number)
            compressed_input += input_to_compress[uncompressed_character]
            return compressed_input
        elif input_to_compress[uncompressed_character] == input_to_compress[uncompressed_character +1]:
            string_match_number += 1
        else:
            compressed_input += str(string_match_number)
            compressed_input += input_to_compress[uncompressed_character]
            string_match_number = 1

final_compress = compress(input('PLease type something to compress:'))
print(final_compress)
