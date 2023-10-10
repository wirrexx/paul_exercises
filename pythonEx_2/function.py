""" def full_name (first, last, profession = "Programmer"):
    return f"Hello {first} {last}, hope you are doing good, I guess you are a {profession} to be!"

x = print(full_name("Wisam", "Odish"))
d = print(full_name("Patrick", "Kluivert"))


def user_full_name(*args):
    return f"One famous singer is {args[0]} {args[1]}"


friend = user_full_name("James", "Brown")
print(friend)


 """

""" def add_numbers(*numbers):
    nums = 0 
    for x in numbers:
        nums += x
    return nums

x = add_numbers(1,2,34,5,6,6,7,999,6)
print(x) """




""" # unpacking in general
my_list=[11,22,10,4,5,6,7,8]
x1, x2, x3, x4, x5, x6, x7, x8 = my_list
print(x2) """


#Unpacking of function arguments, i.ex unpacking collection. 
def multiply_by_x(*args):
    multi = 0
    for x in args:
        multi += x
    return multi

my_list=[11,22,10,4,5,6,7,25]
my_numbers = multiply_by_x(*my_list)
print(my_numbers)