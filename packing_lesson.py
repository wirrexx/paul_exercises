""" # packing and unpacking

shopping_basket: list = [1, 2, 3, 4, 5, 6]

# list and tuples * (unpacking) (packing)

num1, *num_rest = shopping_basket

print(num1, num_rest)


# packing and unpacking in a func

def get_all_values(*values):
    a, b, *c = values
    print(f"values {values}")


function_values: list = [1, 4, 5, 6, 'shoes', 'german']
get_all_values(*function_values)
"""
# -------------------------------------------------------#
from pprint import pprint
# List of items
# shopping_List: list = ['Shoes', 'shirt', 'cat']

# function with all positional args.


""" def function_1(arg1, arg2, arg3):
    pprint(arg1)
    pprint(arg2)
    pprint(arg3) """


# function_1(*shopping_List)

# fucntion with combination of keyword and positional arguments.
""" 
def function_2(arg1, arg2, arg3=None):
    pprint(arg1)
    pprint(arg2)
    pprint(arg3) """


# function_2(*shopping_List, list, tuples)

""" def function_3(*shopping_List):
    pprint(shopping_List)
    pprint(shopping_List[0])


function_3(*shopping_List)

"""
# ** unpacking packing
# 1. ** works for dictionaries alone in function call.
# 2. ** works for keyword arguments in function definition. (doesnt work with positional arguments)


def function_4(**items):
    pprint(items)


shopping_list2: dict = {
    'item_1': 'shoes',
    'item_2': 'Shirt',
    'item_3': 'cat'
}


# function_4(**shopping_list2)


def function_5(item_1=None, **items):
    print(item_1)
    print(items)


# function_5(**shopping_list2)

def function_6(item_2, item_1=90, **items):
    pprint(item_2)
    pprint(item_1)
    pprint(items)


# function_6(**shopping_list2)


def function_7(var_a=None, *items):
    print('I got this far')


# function_7(45, 56)


# 1. define a  function with one positional argument called age
# one keyword called location
# collect other information such as name and fav meal


# ** items = skapar en dictionary
def favorite_meal(age, location='Berlin', **items):
    pprint(items)

    # dessa två variablar namn blir key och vad dom hämtar blir values
    fave_meal = items.get('fave_meal')
    name = items.get('name')

    # if there is no name, greet the user as John Doe
    if name is None:
        name = 'John Doe'
    elif name == 'Cristiano':
        pprint('SIIIIU!')

    pprint(f'Hello, {name}')

    # if the persons age is less then 10, print that he is not allowed to have a fav meal
    if age < 10:
        pprint(
            'Unfortunatly, you are not allowed to have a favourite meal, EAT YOUR PEAS!')
    elif fave_meal is not None:
        pprint(f"Your favourite meal is {fave_meal}. ")
    # if the users location is not in berlin, print welcome to berlin
    if location != 'Berlin':
        pprint('Welcome to Berlin!')


favorite_meal(age=24, location='Madrid', fave_meal='Pizza')
