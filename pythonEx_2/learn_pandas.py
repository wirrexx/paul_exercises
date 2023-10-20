import pandas as pd 
from collections import Counter

file = pd.read_csv('turtles.csv')

counter = Counter(file)
print(file)
# info Ger dig information över hur många elements som finns. 54 entries 0-53
print(file.info())
print('-' *50)

print(file.shape)
print('-' *50)
# Kan söka på index namn och nummer, med namn kan man få ut hur lång char det är? 
print(file.loc[2])


print(counter)