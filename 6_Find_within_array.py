# We'll create a function that takes in two parameters:
#
# a sequence (length and types of items are irrelevant) a function (value, index) that will be called on members of
# the sequence and their index. The function will return either true or false. Your function will iterate through the
# members of the sequence in order until the provided function returns true; at which point your function will return
# that item's index.
#
# If the function given returns false for all members of the sequence, your function should return -1.
#
# true_if_even = lambda value, index: value % 2 == 0
# find_in_array([1,3,5,6,7], true_if_even) # --> 3

true_if_even = lambda v, i: v % 2 == 0
never_true = lambda v, i: False
true_if_value_equals_index = lambda v, i: v == i
true_if_length_equals_index = lambda v, i: len(v) == i


def find_in_array(seq, predicate):
    for i, elem in enumerate(seq):
        if predicate(elem, i):
            return i
    return -1


z = find_in_array([1, 3, 5, 6, 7], true_if_even)
print(z)
