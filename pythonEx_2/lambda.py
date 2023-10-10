# if_bigger = lambda x: True if x > 0 else False
# print(if_bigger(3))



def is_bigger():
    x=3 
    return "bigger" if x > 0 else "smaller"


variable = is_bigger()

print(variable)

add_num = lambda x,y,z: x+y+z

print(add_num(4,5,6))


# complex

my_dict = {"A": 1, "B": 2, "C": 3}
print(sorted(my_dict, key=lambda x: my_dict[x]%3)) # Returns ['C', 'A', 'B']

