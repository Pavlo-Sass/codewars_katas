def parse_molecule (formula):
    answer = {}
    multipl = 1
    for elem in range(len(formula)):
        if formula[elem].isalpha():
            answer[formula[elem]] = 1




a = parse_molecule("K4[ON(SO3)2]2")