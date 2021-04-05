# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return
# true if the string is valid, and false if it's invalid.
#
# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}.
# Thanks to @arnedag for the idea!
#
# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
#
# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.
#
# Examples
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False

def validBraces(string):
    nstr = string.replace('[', chr(92)).replace('{', chr(124))
    k = 0
    a = ['0']
    for i in range(0, len(nstr)):
        if ord(''.join(a[k])) == ord(nstr[i]) - 1:
            a.pop()
            k -= 1
        else:
            a.append(nstr[i])
            k += 1
    if len(a) == 1:
        return True
    return False

print(validBraces("[({})](]"))