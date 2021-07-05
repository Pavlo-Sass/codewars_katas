# 1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246. Squaring these divisors we get: 1, 60516, 4, 15129, 9,
# 6724, 36, 1681. The sum of these squares is 84100 which is 290 * 290.
#
# Task Find all integers between m and n (m and n integers with 1 <= m <= n) such that the sum of their squared
# divisors is itself a square.
#
# We will return an array of subarrays or of tuples (in C an array of Pair) or a string. The subarrays (or tuples or
# Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the
# squared divisors.
#
# Example:
# list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
# list_squared(42, 250) --> [[42, 2500], [246, 84100]]
# The form of the examples may change according to the language, see "Sample Tests".
#
# Note In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing
# whitespace: you can use dynamically allocated character strings.

import math


def list_squared(m, n):
    answ = []
    for i in range(m, n + 1):
        div = []
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                div.append(j ** 2)
                if j != i / j:
                    div.append((i / j) ** 2)
        total = sum(div)
        if math.sqrt(total) % 1 == 0:
            answ.append([i, int(total)])
    return answ

a = list_squared(1, 250)
print(a)
