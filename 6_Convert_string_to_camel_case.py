# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
# within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case,
# also often referred to as Pascal case).
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re


def to_camel_case(text):
    if text == '':
        return text
    match = re.findall(r'([A-Za-z]+)', text)
    answ = match[0]
    for i in range(1, len(match)):
        answ += match[i].capitalize()
    return answ


a = to_camel_case("")
print(a)
