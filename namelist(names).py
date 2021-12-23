def namelist(names):
    # your code here
    # res = [ x.append(names['name']) for name in names for x in xs]
    arr = []
    res = ''
    for name in names:
        arr.append(name['name'])
    print(arr)

    for i, x in enumerate(arr):
        if i == len(arr) - 2:
            res += f'{x} & {arr[len(arr) - 1]}'
            break
        res += f'{x}, ' 
        
    return res


a = namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])
b = namelist([{'name': 'Bart'},{'name': 'Lisa'}])
c = namelist([{'name': 'Bart'}])
print(a)