# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The
# function should return true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100
#
# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the
# input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as
# parentheses (e.g. [], {}, <>).


def valid_parentheses(string):
    query = [None]
    for char in string:
        if char == '(':
            query.append(char)
        elif char == ')':
            if query.pop(-1) != '(':
                return False
    if len(query) == 1:
        return True
    else:
        return False

a = valid_parentheses("hi(hi)()")
print(a)
