from operator import itemgetter
from pprint import pprint

""" iterables_list =['string', 'list', 'tuple','dictionary', 1,2,3, False]
iterables_list2 =('string', 'list', 'tuple','dictionary', 1,2,3, False) """
iterables_list3 ={'string':'ord', 'tuple':'dictionary', (1,2,3): False}

""" pprint(len(iterables_list))
pprint(range(len(iterables_list))) """

""" # den här listan skriver ut namnet och lopar igenom iterables list. Istället för att bara returnera index
for items in range(len(iterables_list)):
    # iterables_list[items] kallar på namnet, eftersom vi använder rangelen, blir items en index
    pprint(f"Item name: {iterables_list[items]} Item index: {[items]}") """


# ger samma effekt som ovanför, men här räknar vi från 0 till slutet av listan. Counter = index och x = namnet
""" counter = 0
for x in iterables_list2:
    print(f"Item name: {x}, Item index: {[counter]}")
    counter +=1 """

""" 
counter = 0
for x in iterables_list3:
    pprint(f"Item name: {[counter]}, Item index: {iterables_list3[x]}")
    counter +=1
    

print("\t")

counter = 0
for y in iterables_list3.values():
    pprint(f"Item name: {[counter]}, Item index: {y}")
    counter +=1 """

""" 
for x, y in iterables_list3.items():
    pprint (f"The key name is: {x} and the Value name is: {y}") """


for d in iterables_list3.items():
    pprint (f"The key name is: {d[0]} and the Value name is: {d[1]}") 
