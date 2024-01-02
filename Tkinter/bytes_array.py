with open('textinbinary.bin', 'wb') as file:
    binary_data =b'It is christmas time example with binary data generated on the client\'s computer in a text format. we will be converting the tet to binary data using three approaches: (1) bytes and decode, (2) simply prepending b and (3) and we will be relying on encode'

    file.write(binary_data)
    print(type(binary_data))
    print(binary_data)
    print()

    # conversion of bytes to string

    decoded_data = binary_data.decode('utf-8')
    print(decoded_data)
    print()

    # Let's peek into data
    print(decoded_data[0])
    print(binary_data[0])
    
    print(f'binary repres. of a letter \'a\' is {ord("A")}.')
    print(f'binary repres. of a letter \'Z\' is {ord("Z")}.')
    print(f'binary repres. of a letter \'a\' is {ord("a")}.')
    print(f'binary repres. of a letter \'z\' is {ord("z")}.')
    print(f'binary repres. of a letter \'Ö\' is {ord("Ö")}.')
    print(f'binary repres. of a letter \'م\' is {ord("م")}.')
    
    
    # Len method
    print(len(decoded_data))
    print(len(binary_data))
    
    # Generate Error by replacing 73 with a letter
    try: 
        binary_data[0] =b'Y'
        binary_data[0] ='Y'
    except TypeError:
        print('\'Bytes object does not support item assignment\'')
        
    # Bytearray
    
    b_array_content = bytearray(b'Hello')
    print(b_array_content)
