# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to
# match str2, otherwise returns false.
#
# Notes:
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered
# Input strings s1 and s2 are null terminated.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

# def scramble(s1, s2):
#     array = list(s1)
#     try:
#         for char in s2:
#             array.remove(char)
#         return True
#     except:
#         return False
# def scramble(s1, s2):
#     for char in s2:
#         if s2.count(char) > s1.count(char):
#             return False
#     return True
def scramble(s1, s2):
    for char in set(s2):
        if s2.count(char) > s1.count(char):
            return False
    return True



# a = scramble('cedewaraaossoqqyt', 'codewars')
# a = scramble('katas', 'steak')
a = scramble('pbzyaopfqvpxu', 'ybqaopuvpfzpx')
print(a)