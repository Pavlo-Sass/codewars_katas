def valid_parentheses(string):
    query = [None]
    for char in string:
        if char == '(':
            query.append(char)
        elif char == ')':
            if query.pop(-1) != '(':
                return False
    if len(query) == 1:
        return True
    else:
        return False

a = valid_parentheses("hi(hi)()")
print(a)
