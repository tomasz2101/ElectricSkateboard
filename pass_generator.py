from os import urandom
from random import choice
import sys

char_set = {'small': 'abcdefghijklmnopqrstuvwxyz',
            'nums': '0123456789',
            'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'special': '^!\$%&/()=?{[]}+~#-_.:,;<>|\\'
            }


def generate_pass(length=21):
    """Function to generate a password"""

    password = []

    while len(password) < length:
        key = choice(char_set.keys())
        a_char = urandom(1)
        if a_char in char_set[key]:
            if check_prev_char(password, char_set[key]):
                continue
            else:
                password.append(a_char)
    return ''.join(password)


def check_prev_char(password, current_char_set):
    """Function to ensure that there are no consecutive 
    UPPERCASE/lowercase/numbers/special-characters."""

    index = len(password)
    if index == 0:
        return False
    else:
        prev_char = password[index - 1]
        if prev_char in current_char_set:
            return True
        else:
            return False


if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        print(generate_pass(int(sys.argv[1])))
    else:
        length = input('Give password length:  ')
        print(generate_pass(length))
