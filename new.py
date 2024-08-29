import string
import keyword


def is_valid_variable_name(variable_name):

    if variable_name in keyword.kwlist:
        return False


    if variable_name[0].isdigit():
        return False


    if any(char.isupper() for char in variable_name):
        return False


    allowed_chars = string.ascii_lowercase + string.digits + '_'
    if any(char not in allowed_chars for char in variable_name):
        return False


    if variable_name.count('_') > 1:
        return False

    return True


# Приклади
print(is_valid_variable_name("new_name"))
print(is_valid_variable_name("newName"))

