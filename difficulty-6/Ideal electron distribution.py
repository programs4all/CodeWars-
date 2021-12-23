
def atomic_number(electrons):
    shells, i = [], 1
    while sum(shells) + 2 * i ** 2 < electrons:
        shells.append(2 * i ** 2)
        i += 1
    if electrons - sum(shells):
        shells.append(electrons - sum(shells))
    return shells

# def atomic_number(electrons):
#     shells = []
#     i = 1
#     while True:
#         calc = 2 * i ** 2
#         print(calc)
#         if sum(shells) + calc >= electrons:
#             print('break')
#             shells.append(electrons - sum(shells))
#             break 
#         shells.append(calc)
#         print(shells)
#         i += 1
#     print(shells)
#     return shells


print(atomic_number(1),[1])
print(atomic_number(10),[2, 8])
print(atomic_number(11),[2, 8, 1])
print(atomic_number(22),[2, 8, 12])
print(atomic_number(23),[2, 8, 13])
print(atomic_number(47),[2, 8, 18, 19])
print(atomic_number(50),[2, 8, 18, 22])
print(atomic_number(52),[2, 8, 18, 24])
print(atomic_number(60),[2, 8, 18, 32])
print(atomic_number(61),[2, 8, 18, 32, 1])