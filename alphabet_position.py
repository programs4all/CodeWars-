


def alphabet_position(text):
    alph = list('abcdefghijklmnopqrstuvwxyz')
    res = []
    for char in text.lower():
        if char.isalpha():
            idx = alph.index(char)
            res.append(str(idx + 1))
            
    return ' '.join(res)


a = alphabet_position("The sunset sets at twelve o' clock.")
print(a)