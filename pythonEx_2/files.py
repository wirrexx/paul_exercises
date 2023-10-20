from pprint import pprint
f = open('turtles.csv', 'w')
print (f.writable())
f.write('Welcome to the world of files.')

f.close()


f = open('turtles.csv')

lines = f.readlines()

for x in lines:
    print(x)