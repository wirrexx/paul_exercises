from operator import itemgetter
from pprint import pprint

iterables_list =['string', 'list', 'tuple','dictionary', 1,2,3, False]
iterables_list2 =('string', 'list', 'tuple','dictionary', 1,2,3, False)

""" pprint(len(iterables_list))
pprint(range(len(iterables_list))) """

# den här listan skriver ut namnet och lopar igenom iterables list. Istället för att bara returnera index
for items in range(len(iterables_list2)):
    # iterables_list[items] kallar på namnet, eftersom vi använder rangelen, blir items en index
    pprint(f"Item name: {iterables_list[items]} Item index: {[items]}")


# ger samma effekt som ovanför, men här räknar vi från 0 till slutet av listan. Counter = index och x = namnet
counter = 0
for x in iterables_list2:
    print(f"Item name: {x}, Item index: {[counter]}")
    counter +=1
    