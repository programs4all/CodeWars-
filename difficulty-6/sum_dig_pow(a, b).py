def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    # for a range betweem a - b return a list of all numbers that have the property: 135 = 1^1 + 3^2 + 5^3
    # for num in range(a, b):
    # if num = res:

    end = []
    for integer in range(a, b+1):
#         digits = [int(x) for x in str(integer)]
#         print(digits)
        res = []
        res = sum([pow(num, idx+1) for idx, num in enumerate([int(x) for x in str(integer)])])
        # print(res)
        if res == integer:
            end.append(res)
    # print(end)
    return end

a = sum_dig_pow(1, 135)
print(a)


# cant believe this actuall works 
def comprehesion_sum_dig_pow(a, b):
    return [ integer for integer in range(a, b+1) if integer == sum([pow(num, idx+1) for idx, num in enumerate([int(x) for x in str(integer)])]) ]

b = comprehesion_sum_dig_pow(1, 135)
print(b)


def clean_sum_dig_pow(a, b):
    return [i for i in range(a,b+1) if sum([pow(num,idx+1) for idx,num in enumerate([int(x) for x in str(i)])])==i]

c = clean_sum_dig_pow(1, 135)
print(c)
