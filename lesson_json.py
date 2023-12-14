import json

x = '{"name": "John", "age": 36}'

# treats it as a dictionary, converts it
dict = json.loads(x)

# prints it as a dictionary
print(dict['age'])
