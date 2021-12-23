def order(sentence):
    # code here
    li = sentence.split(' ')
    hash_map = {}
    res = ''
    
    for word in li:
        for char in word:
            if char.isdigit():
                hash_map[int(char)] = word
                print(hash_map)

    for i in sorted(hash_map):
        res = f'{res}{hash_map[i]} '
        # print(res)
        # print(hash_map[i])

    return res.rstrip()



def order_smart(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))


# a = order("4of Fo1r pe6ople g3ood th5e the2")
# print(a)

b = order_smart("4of Fo1r pe6ople g3ood th5e the2")
print(b)