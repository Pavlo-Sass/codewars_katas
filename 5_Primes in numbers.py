# Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the
# following form :
#
#  "(p1**n1)(p2**n2)...(pk**nk)"
# where a ** b means a to the power of b
#
# with the p(i) in increasing order and n(i) empty if n(i) is 1.
#
# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

def prime_factors(number):
    result = []
    answer = ''
    i = 2
    while number > 1:
        if number % i == 0:
            number = number/i
            result.append(i)
        else:
            i += 1
    i_prev = None
    for i in result:
        if i_prev != i:
            if result.count(i) > 1:
                answer = answer + f'({i}**{result.count(i)})'
                i_prev = i
            else:
                answer = answer + f'({i})'
    return answer

a = 933555431
print(prime_factors(a))