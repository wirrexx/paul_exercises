
# day 1 exercise with functions
print('Welcome to the Band Name Generator.')

def city_name():
    city_name = input("What's name of the city you grew up in?\n")
    return city_name

    
def pet_name():
    pet_name = input("What's your pet's name?\n")
    return pet_name


name_of_city = city_name()
name_of_pet = pet_name()

result = f'Your band name could be {name_of_city} {name_of_pet}'

print(result)

# day 1 exercise using classes


class City:
    def __init__(self):
        pass
    
    def city_name(self):
        city_name = input("What's name of the city you grew up in? \n")
        return city_name
        
class Pet:
    def __init__(self):
        pass
    
    def pet_name(self):
        pet_name = input("What's your pet's name?\n")
        return pet_name
            
        


new_city = City()
new_pet = Pet()

result = f'Your band name could be {new_city.city_name()} {new_pet.pet_name()}'
print(result)