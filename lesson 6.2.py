import string
def get_characters_between(letters):
       all_letters = string.ascii_letters
       start_letter, end_letter = letters.split('-')

       start_index = all_letters.index(start_letter)
       end_index = all_letters.index(end_letter)

       return all_letters[start_index:end_index+1]

user_input = input("Введите 2 буквы: ")
result = get_characters_between(user_input)
print(result)

