x = 10 
y = 'My string'
my_list = ['1','2','3','4']
is_married = True
my_dict: dict = {
    'name':'Wisam', 
    'age': 36,
    }

class A: 
    secret: 12
    def __len__(self):
        return 
    
    

a = A()

# print(len(x))  False on int ,float
print(len(y)) # True on string
# print(len(is_married))  False on boolean
print(len(my_list))
print(len(my_dict))
print(len(a))