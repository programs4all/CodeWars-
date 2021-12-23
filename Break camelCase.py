def solution(s):
    li = [x for x in s]
    print(li)
    spaces = []
    for idx, char in enumerate(li):
        print(idx)
        if char.isupper():
            spaces.append(idx)
        
    for num in spaces:
        li.insert(num, ' ')

    return ''.join(li)

a = solution('helloWorld')
print(a)