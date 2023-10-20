a_list = [1,2,3,4,5]
def by_two(el):
    return el ** 6



result = map(by_two, a_list)
print(result)
print(list(result))

print('*' *50)


def is_odd(el):
    return el % 2 != 0

result2 = filter(is_odd, a_list)
print(result2)
print(list(result2))
