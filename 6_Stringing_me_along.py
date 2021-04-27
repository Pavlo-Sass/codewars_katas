# Description: Implement a function that receives a string, and lets you extend it with repeated calls. When no
# argument is passed you should return a string consisting of space-separated words you've received earlier.
#
# Note: there will always be at least 1 string; all inputs will be non-empty.
#
# For example:
#
# create_message("Hello")("World!")("how")("are")("you?")() == "Hello World! how are you?"


def create_message(s, list=[]):
    def sub_func(z=None):
        if z == None:
            answ = " ".join(list)
            list.clear()
            return answ
        else:
            return create_message(z, list)

    list.append(s)
    return sub_func


# b = create_message("Hello")("5")("6")()
b = create_message("Hello")("World!")("how")("are")("you?")("this")("is")("less")()
# Hello World! how are you? this is less
print(b)
