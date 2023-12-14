from abc import ABC, abstractmethod

# vad kan vi göra med en fil
# open read
# edit update
# write
# close

# goals
# klass som kan göra alla steg ovanför för Json filer
# klass som kan göra alla steg ovanför för csv filer
# klass som kan göra alla steg ovanför för txt filer

# Inheritance
# abstraction
# polymorphism

# new_file = Json('shopping_data.json')
# new_file.read()
# new_file.write()


# inheritance and Abstract classes only

class Files(ABC):
    def __init__(self, file_name: str = '') -> None:
        self.filename = file_name
        self.get_file_type()  # parent class

    @abstractmethod
    def get_file_type(self):  # viktig metod för child klasser
        print(f'File type is txt')

    @abstractmethod  # viktig metod för barn klasser, olika sätt att läsa filer
    def read(self):
        print(f'Read file')

    def update(self):
        print(f'Updated file')

    def write(self, data={}):
        print(f'Wrote to file')

    def close(self):
        print('Closing the current file.')

    def save(self):
        print(f'Saved file to {self.filename} ')


class Json(Files):
    # om du inte implementerar get_file_type, jag kommer att flagga på en error
    def get_file_type(self):  # viktig metod för child klasser
        print(f'File type is .json')

    def read(self):
        print(f'Read json file')


class Csv(Files):
    def get_file_type(self):  # viktig metod för child klasser
        print(f'File type is .csv')

    def read(self):
        print(f'Read csv file')


class Txt(Files):
    def get_file_type(self):
        return super().get_file_type()

    def read(self):
        print(f'Read txt file')


""" new_json_file = Json('shop_data.json')
print('-'*25)
new_csv_file = Csv('data.csv')
shop_information = Csv('shop_data.csv')
"""

""" list_of_file_workers = [new_json_file, new_csv_file, shop_information]
for file in list_of_file_workers:
    file.read() """

""" 
class Utility:
    def display(self, file_class):
        print(file_class.filename)


help = Utility()
help.display(new_csv_file)
"""


# Arbetar på supermarket
# 1. varje dag får vi en lista av filer från en server
# 2. vi vill läsa filerna och spara dom någon annanstans
# 3. 2023/11/20

def file_class_factory(file_name, *args, **kwargs):
    # helps me to select a class
    if file_name.endswith('.csv'):
        # removing brackets, makes it a class factory
        file_class = Csv
    elif file_name.endswith('.json'):
        file_class = Json
    else:
        file_class = Txt
    return file_class


def file_object_factory(file_name, *args, **kwargs):
    # helps me to select a class
    if file_name.endswith('.csv'):
        # leaving the brackets, makes it a class object
        file_class = Csv(file_name)
    elif file_name.endswith('.json'):
        file_class = Json(file_name)
    else:
        file_class = Txt(file_name)
    return file_class


list_of_files = ['a.csv', 'b.json', 'c.txt', 'd.json', 'e.csv', 'f.txt']

# class factory calling
for file_name in list_of_files:
    file_class = file_class_factory(file_name)
    file_object = file_class(file_name)
    file_object.read()
    file_object.save()

# object factory calling
for file_name in list_of_files:
    file_object = file_object_factory(file_name)
    file_object.read()
    file_object.save()
