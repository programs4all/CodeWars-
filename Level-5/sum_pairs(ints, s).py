def sum_pairs(ints, s):
    res = []
    for idx, num in enumerate(ints):
        search = s - num
        for idx2, num2 in enumerate(ints):
            if num2 == search and idx != idx2:
#                 print(num, num2)
                res.append(([num, num2],[idx, idx2]))
    print(res)
    if len(res) > 1:
        for i in range(len(res) - 1):
#             print(res[i][1])
            high = max(res[i][1])
        #         print(high)
            if max(res[i+1][1]) < high:
                low = res[i+1][0]
            else:
                low = res[i][0]
        print(list(low))
        return low
    else:
        return res