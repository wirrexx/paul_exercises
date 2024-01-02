from io import BytesIO, StringIO

data = b'Hello, binary world!'

print('Binary data: ', data)

with BytesIO(data) as stream:
    content=stream.read()
    
print('Decoded data: ', content.decode())

import csv

data_new = """name, Age, City, 
John, 25, New York, 
Alice, 30, San Francisco"""

with StringIO(data_new) as stream:
    
    reader = csv.reader(stream)
    
    for row in reader:
        print(row)


import base64

binray_data = b'Hello, ASCII Armor!'

"""ASCII-Armor, also known as ASCII Armor. Technique to convert binary data into text format. Ensures encoding that the data remains intact when transmitted or shared across systems or platforms,
which might otherwise get corrupted. Often employed in an email """

armored_data = base64.b64encode(binray_data).decode('utf-8')
print('Original Binary Code: ', binray_data)
print('Armored Binary Code: ', armored_data)


with open('original.png', 'rb') as file: 
    contents = file.read()
    armored_image = base64.b64encode(contents)
    print('Armored File: ', armored_image)
    file.seek(0)
    print('Original File: ', file.read())
