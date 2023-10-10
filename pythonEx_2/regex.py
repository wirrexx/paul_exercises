# --- REGEX TASK ---

from re import (
    findall,
    search, 
    IGNORECASE,
    split, 
    sub,
)

poem = "It matters not how strait the gate, How charged with punishments the scroll, I am the master of my fate, I am the captain of my soul."

my_list = findall("[a-zA-z]", poem)
my_search = search("how", poem, flags=IGNORECASE) #ignores upperCase 
my_split = split(',', poem)

print(my_list)
print('*'*40)
print(type(my_search.span())) #returns tuple instead of re.Match. 
print('*'*40)
print(my_split)