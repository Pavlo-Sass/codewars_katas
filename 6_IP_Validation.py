# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if
# they consist of four octets, with values between 0 and 255, inclusive.
#
# Input to the function is guaranteed to be a single string.
#
# Examples
# Valid inputs:
#
# 1.2.3.4
# 123.45.67.89
# Invalid inputs:
#
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Note that leading zeros (e.g. 01.02.03.04) are considered invalid.

def is_valid_IP(strng):
    lst = strng.split('.')
    if len(lst) != 4:
        return False
    for num in lst:
        if num[0] == '0' and len(num) > 1:
            return False
        elif not num.isdigit():
            return False
        elif 0 > int(num) or int(num) > 255:
            return False
    return True


data = '192.168.1.300'
a = is_valid_IP(data)
print(a)
