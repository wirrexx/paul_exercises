# Vad är en collection 
# Låter dig visualisera set of item (collection)

# string är också ett sett av character Hello world = h,e,l,l,o'',w,o,r,l,d
# for loops för att accessera individuella "delar" av collectionen. 

""" Advantage: 
1. You can add and remove elements quickly. 
2. Does not require reorganizing the data structure unlike arrays or list. 
3. Linear data structure.

Disadvantage
1. More memory is required when compared to an array. Because you need pointers, which takes up its own memory, to point you to the next element
2. search oepration on a linked list are very slow, unlike an array. You dont have the option of random access 

When Should You Use a Linked List?

    You don't know how many items will be in the list (that is one of the advantages - ease of adding items).
    You don't need random access to any elements (unlike an array, you cannot access an element at a particular index in a linked list).
    You want to be able to insert items in the middle of the list.
    You need constant time insertion/deletion from the list (unlike an array, you don't have to shift every other item in the list first).
"""


table =[['heading', 'heading2','dumbo'],
            [123,456,789, 234,242],
            [True,False,True]
            ]

for row in table: 
    print(row[:2])