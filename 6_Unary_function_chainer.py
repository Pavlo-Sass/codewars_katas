# Your task is to write a higher order function for chaining together a list of unary functions. In other words,
# it should return a function that does a left fold on the given functions.
#
# chained([a,b,c,d])(input)
# Should yield the same result as
#
# d(c(b(a(input))))

def f1(x):
    print('f1')
    return x * 2.0
def f2(x):
    print('f2')
    return x + 2
def f3(x):
    print('f3')
    return x ** 2

def f4(x):
    print("f4 = ", x)
    return x.split()
def f5(xs):
    print("f5 = ", xs)
    return [x[::-1].title() for x in xs]

def f6(xs):
    print("f6 = ", xs)
    return "_".join(xs)

def chained(list):
    list = list[:]
    def subfunk(x):
        if len(list) > 0:
            funk = list.pop()
            a = subfunk(x)
            return funk(a)
        else:
            return x
    return subfunk

res = chained([f4,f5,f6])('337Yik9Qr96Zlmwmrhw7Iftryq0Eut4N')
print(res)