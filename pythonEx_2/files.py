import os
from pprint import pprint
# 4 mods 
# r - read
# a - append
# w - Write
# x - create
# b - binary (pictures to be opened)  måste komma i slutet av en av dom första mods så open('wisam.jpeg', 'rb')
# t - text 
from PIL import Image
f = open('./Pictures/sw.jpg','w')
print (f.writable())
f.writelines('Welcome to the world of files.\n')
f.write('now get the f out')

f.close()


f = open('turtles.csv')

lines = f.readlines()

for x in lines:
    print(x)


os.remove ('turtles.csv')