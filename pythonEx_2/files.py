import os
from pprint import pprint
f = open('turtles.csv', 'a')
print (f.writable())
f.writelines('Welcome to the world of files.\n')
f.write('now get the f out')

f.close()


f = open('turtles.csv')

lines = f.readlines()

for x in lines:
    print(x)


os.remove ('turtles.csv')