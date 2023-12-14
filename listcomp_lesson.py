# list, sets, generators, dict
# online for loop, filter, result

# det här är korta versionen av(kolla under)
names: list = [(item+100) for item in range(1, 6) if item % 2 == 0]

shoes: dict = {'nike': 'jordan', 'adidas': 'predator'}
items = {(value) for value in shoes.values()}

# det här
all_name = []
for x in range(1, 6):
    if x % 2 == 0:
        all_name.append(x)

print(all_name)
print(names)
print(items)
