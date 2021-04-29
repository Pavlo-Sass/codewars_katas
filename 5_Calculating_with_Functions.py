# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine") There must be a function for each of the
# following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python) Each calculation
# consist of exactly one operation and two numbers The most outer function represents the left operand,
# the most inner function represents the right operand Division should be integer division. For example, this should
# return 2, not 2.666666...:

def zero(fn = None):
    x = 0
    if fn == None:
        return x
    else:
        return int(fn(x))

def one(fn = None):
    x = 1
    if fn == None:
        return x
    else:
        return int(fn(x))

def two(fn = None):
    x = 2
    if fn == None:
        return x
    else:
        return int(fn(x))
def three(fn = None):
    x = 3
    if fn == None:
        return x
    else:
        return int(fn(x))
def four(fn = None):
    x = 4
    if fn == None:
        return x
    else:
        return int(fn(x))

def five(fn = None):
    x = 5
    if fn == None:
        return x
    else:
        return int(fn(x))

def six(fn=None):
    x = 6
    if fn == None:
        return x
    else:
        return int(fn(x))

def seven(fn = None):
    x = 7
    if fn == None:
        return x
    else:
        return int(fn(x))

def eight(fn = None):
    x = 8
    if fn == None:
        return x
    else:
        return int(fn(x))

def nine(fn = None):
    x = 9
    if fn == None:
        return x
    else:
        return int(fn(x))

def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x / y


z = 8

a = seven(times(five()))
print(a)