my_string = "Hello Coder! You have done it! "

iterator = iter(my_string)


while True: 

    item = next(iterator, 'end')
    if item == 'end':
        break
    print(item)