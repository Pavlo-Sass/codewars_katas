# Description:
# A
# simple
# substitution
# cipher
# replaces
# one
# character
# from an alphabet
#
# with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the
# alternate alphabet for encoding or decoding.
#
# E.g.
#
# map1 = "abcdefghijklmnopqrstuvwxyz";
# map2 = "etaoinshrdlucmfwypvbgkjqxz";
#
# cipher = Cipher(map1, map2);
# cipher.encode("abc")  # => "eta"
# cipher.encode("xyz")  # => "qxz"
# cipher.encode("aeiou")  # => "eirfg"
#
# cipher.decode("eta")  # => "abc"
# cipher.decode("qxz")  # => "xyz"
# cipher.decode("eirfg")  # => "aeiou"
# If
# a
# character
# provided is not in the
# opposing
# alphabet, simply
# leave
# it as be.


# MY FIRST SOLUTION


# class Cipher(object):
#     def __init__(self, map1, map2):
#         self.map1 = map1
#         self.map2 = map2
#
#     def encode(self, s):
#         answ = ""
#         for char in s:
#             if char in self.map1:
#                 answ += self.map2[self.map1.index(char)]
#             else:
#                 answ += char
#         return answ
#
#     def decode(self, s):
#         answ = ""
#         for char in s:
#             if char in self.map2:
#                 answ += self.map1[self.map2.index(char)]
#             else:
#                 answ += char
#         return answ

# MY SECOND SOLUTION

class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2

    def encode(self, s):
        encdng = str.maketrans(self.map1, self.map2)
        return s.translate(encdng)

    def decode(self, s):
        dcdng = str.maketrans(self.map2, self.map1)
        return s.translate(dcdng)

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";
cipher = Cipher(map1, map2)
a = cipher.encode("abc8")
print(a)