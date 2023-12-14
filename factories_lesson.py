# Class factory using a function that returns a Class definition
# which will be invoked and given a name during runtime


# function factorys
def create_factory(has_wheels, num_wheels):
    class factory:
        def __init__(self, **kwargs):

            self.has_wheels = has_wheels
            self.num_wheels = num_wheels
            self.properties = kwargs

    return factory


Car = create_factory(True, 4)
print(Car)

Plane = create_factory(True, 3)
print(Plane)

MotorCycle = create_factory(True, 2)
print(MotorCycle)

# du kan endast skriva ny "keyword arguments" om du har dom uppe i factory parameter
car1 = Car(name='Volvo', horsepower=128)
plane1 = Plane(name='Ferrari', engine_type='V12')

# här kallar du på den
print(car1.properties['name'])
print(plane1.properties)
print(type(car1))
