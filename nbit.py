# dp = 0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

# dp = list('1'*253)
# dp.append('0')
# dp.append('0')
# dp.append('0')
# print(dp)
# from itertools import permutations
#
# perm = list(permutations(dp,2))
# print(perm)


from itertools import product
for i in product(list(range(0,256)),repeat=3):
    n = (((1<<i[0]) | (1<<i[1]) | (1<<i[2]))) ^ 0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    print(n)
    print(bin(n))