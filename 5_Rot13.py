# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the
# alphabet. ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
# characters included in the string, they should be returned as they are. Only letters from the latin/english
# alphabet should be shifted, like in the original Rot13 "implementation".
#
# Please note that using encode is considered cheating.

ABC = 'abcdefghijklmnopqrstuvwxyz'


def rot13(message):
    answer = ''
    for char in message:
        if char.lower() not in ABC:
            answer += char
            continue
        index = (ABC.index(char.lower()) + 13) % 26
        if char.isupper():
            answer += ABC[index].upper()
        else:
            answer += ABC[index]
    return answer


a = "Pbqrjnef"
b = rot13(a)
print(b)
