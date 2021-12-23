
# alot of room for optimization
# reduce the amount of seperate loops by condensing processes
# reduce the amount of the appendings to lists
# remove redundant operations
def sort_array(array):
    # Return a sorted array.
    odd = []
    even = []
    # seperates index and number of array in to seperate lists deifned by odd and even
    for idx, num in enumerate(array):
        if num % 2:
            odd.append((num, idx))
        else:
            even.append((num, idx))
    
    sort_odd = sorted(odd)
#     print(sort_odd)
    

    # sorted even numbers are re-indexed by a counter that regress by 1 each loop
    res1 = []
    cnt = len(sort_odd) - 1
    for x in sort_odd:
        res1.append((x[0], sort_odd[cnt][1]))
        cnt -= 1
#     print(res1)
#     print(even)
      
        
    #  combines odd and even back into a single list based on the second item in tuple which is the index
    test = res1 + even
    # print(test)
    end_dict = {}
    for k, v in test:
        end_dict[v] = k

    
    res2 = sorted(end_dict.items())
    print(res1)
    res = []

    for k, v in res2:
        print(k, v)
        res.append(v)

    print(res)
    return res


a = sort_array([5, 3, 2, 8, 1, 4])
a1 = [1, 3, 2, 8, 5, 4]
b = sort_array([5, 3, 1, 8, 0])
b1 = [1, 3, 5, 8, 0]
c = sort_array([5, 3, 2, 8, 1, 4, 11])
c1 = [1, 3, 2, 8, 5, 4, 11]
d = sort_array([2, 22, 37, 11, 4, 1, 5, 0])
d1 = [2, 22, 1, 5, 4, 11, 37, 0]
e = sort_array([1, 111, 11, 11, 2, 1, 5, 0])
e1 = [1, 1, 5, 11, 2, 11, 111, 0]

print('----RESULTS----')
print(c, '\n', c1)
print(d, '\n', d1)
print(e, '\n', e1)


def new_sort_array(array):
    pass