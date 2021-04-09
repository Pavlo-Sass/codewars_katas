# Description:
# For a given chemical formula represented by a string, count the number of atoms of each element contained in the
# molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).
#
# For example:
#
# water = 'H2O'
# parse_molecule(water)                 # return {H: 2, O: 1}
#
# magnesium_hydroxide = 'Mg(OH)2'
# parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}
#
# var fremy_salt = 'K4[ON(SO3)2]2'
# parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
# As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to
# multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two
# nitrogen atoms and six oxygen atoms.
#
# Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.

import re

def parse_molecule (formula):
    elements = {}
    # changing all types of braces to round
    # creating dict of braces
    dict = {
        '[': '(',
        ']': ')',
        '{': '(',
        '}': ')'
    }
    # changing braces in loop
    for k, v in dict.items():
        formula = formula.replace(k, v)
    # opening braces and multiple element quantity to index after braces
    # while braces in formula
    while '(' in formula:
        # finding text in braces and index after braces
        match = re.search(r"\(([^()]+)\)(\d)?", formula)
        # text in braces
        exp = match.group(1)
        # index after braces
        mult = match.group(2)
        #checking if index after braces is not None and set string slice where our text in braces ends
        if mult:
            mult = int(mult)
            end = match.end(2)
        else:
            mult = 1
            end = match.end(1)
        # getting tuples of elements and their quantities
        list_match = re.findall(r'([A-Z]+?[a-z]?)(\d*)?', exp)
        new_exp = ''
        # multiplying elements quantities by index after braces
        for elem, quantity in list_match:
            if quantity:
                new_exp += elem + str(int(quantity) * mult)
            else:
                new_exp += elem + str(mult)
        # pasting our part of formula back to main
        formula = formula[:match.start(1)-1] + new_exp + formula[end:]

    # creating final dict
    list_match = re.findall(r'([A-Z]+?[a-z]?)(\d*)?', formula)
    for elem, quantity in list_match:
        if quantity:
            quantity = int(quantity)
        else:
            quantity = 1
        if elem in elements.keys():
            elements[elem] += quantity
        else:
            elements[elem] = quantity
    return elements


a = parse_molecule("Pd[P(C6H5)3]4")
print(a)