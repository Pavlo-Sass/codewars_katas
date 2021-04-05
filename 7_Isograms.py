# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.
# Ignore letter case.

# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case

# my first solution

# def is_isogram(string):
#     a = []
#     for char in string:
#         a.append(char.lower())
#     return len(set(a)) == len(string)

# my second solution

def is_isogram(string):
    return len(string) == len(set(string.upper()))

print(is_isogram('moon'))