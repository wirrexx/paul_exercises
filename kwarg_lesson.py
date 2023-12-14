class A:
    def __init__(self, **kwargs):
        self.person = kwargs

    def show(self):
        for value in self.person.values():
            print(f'{value}')


a = A(name='Robin', country='Sweden', hair_color='Brown')
b = A(name='Wisam', country='Iraq', is_married=True)
c = A(name='AJ', occupation='Studying', has_children=False)


print('\nWho is behind door A?')
a.show()
print('_'*25)

print('\nWho is behind door B?')
b.show()
print('_'*25)

print('\nWho is behind door C?')
c.show()
