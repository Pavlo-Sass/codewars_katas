# Напиши декоратор, який буде рахувати скільки разів викликається функція. Це популярне завдання на співбесідах.
# Звісно глобальну змінну не використовувати.

# def counting(fn):
#     count = 0
#     def wrapper(*args):
#         nonlocal count
#         count += 1
#         print(f'The function was called {count} times ')
#         return fn(*args)
#     return wrapper
#
# @counting()
# def add(*args):
#     res = 0
#     for arg in args:
#         res += arg
#     return res
#
# a = add(1)
# print(a)
# a = add(1, 2)
# print(a)
# a = add(1)
# print(a)
# a = add(1, 2)
# print(a)

def counting(*a):
    text = ''.join(a)
    count = 0
    def wrawrapper(fn):
        def wrapper(*args):
            nonlocal count
            count += 1
            print(text, count)
            return fn(*args)
        return wrapper
    return wrawrapper


@counting('This ', 'is ', 'the ', 'call ', 'number: ')
def add(*args):
    res = 0
    for arg in args:
        res += arg
    return res

a = add(1)
print(a)
