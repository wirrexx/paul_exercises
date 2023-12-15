with open('textinbinary.bin', 'wb') as file:
    text = 'It is christmas time example with binary data generated on the client\'s computer in a text format. we will be converting the tet to binary data using three approaches: (1) bytes and decode, (2) simply prepending b and (3) and we will be relying on encode'
    
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