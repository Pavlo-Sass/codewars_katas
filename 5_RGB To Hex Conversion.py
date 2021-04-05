# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must
# be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# The following are examples of expected output values:
#
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
    colors = [r, g, b]
    text = ''
    for i in range(len(colors)):
        if colors[i] > 255: text = text + 'FF'
        elif colors[i] <= 0: text = text + '00'
        elif colors[i] <= 16: text = text + f"0{hex(colors[i]).split('x')[-1]}"
        else: text = text + hex(colors[i]).split('x')[-1]

    return text.upper()

a = rgb(-15,275,125)
print(a)