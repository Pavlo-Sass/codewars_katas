#   Complete the function/method (depending on the language) to return true/True when its argument is an array that
#   has the same nesting structures and same corresponding length of nested arrays as the first array.

# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )
#
# # should return False
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
#
# # should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )
#
# # should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

def same_structure_as(example, copy):
    if isinstance(example, list) and isinstance(copy, list):
        if len(example) == len(copy):
            for i in range(len(example)):
                if not same_structure_as(example[i], copy[i]):
                    return False
        else:
            return False
    elif isinstance(example, list) or isinstance(copy, list):
        return False
    return True

a = same_structure_as([1,[1,1]],[2,[2,2]])
print(a)