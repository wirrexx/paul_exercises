list3 = [['heading', 'heading2', 'heading3','heading4'],
         ['one', 'two', 'three', 'four'],
         [123,456,789,5555],
         [333,555,666,3333]
         ]

import numpy as np

my_list = np.array(list3)
print("two dimensional list using nparray: \n", my_list)
print('_' * 50)

twocolumns = my_list[:,0:2] #den här raden går igenom raderna, men skriver endast ut index 0 och 1 
print(twocolumns)
print('_' * 50)

arr = np.array([1, 2, 3, 4])
print(arr[2],',',arr[3])
print('_' * 50)

arr = np.array([[1,2,3,4,5], 
                [6,7,8,9,10]
                ]
                )
print('2nd element on first row: ',arr[0,1])
print('3nd element on second row: ',arr[1,2])
print('_' * 50)
