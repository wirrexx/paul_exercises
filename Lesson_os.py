import os
import shutil
from pprint import pprint

print(f'My current directoryis: {os.getcwd()}')
for x in os.listdir():
    print(x)