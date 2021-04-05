# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
# untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    result = []
    for word in text.split(' '):
        if word in ['.', ',', '!', '?']:
            result.append(word)
        elif word[-1] in ['.', ',', '!', '?']:
            result.append(f'{word[1:-1]}{word[0]}ay{word[-1]}')
        else:
            result.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(result)

a = pig_it('Pig, latin is cool !')
print(a)