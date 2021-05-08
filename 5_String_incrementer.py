# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
#
# Attention: If the number has leading zeros the amount of digits should be considered.

import re

def increment_string(strng):
    text = ''.join(re.findall(r'^(.*\D)(?=\d+)', strng))
    number = re.findall(r'(\d+$)', strng)
    if not number:
        text = strng
        add_number = "1"
    else:
        add_number = str(int(number[0])+1).rjust(len(number[0]),"0")

    return text + add_number

a = increment_string("foo38400080")
print(a)