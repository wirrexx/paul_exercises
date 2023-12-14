# Composition
# vad är composition, Solid principles
# Has-a relationship med andra klasser


class Employee:
    def __init__(self, name, salary=0) -> None:
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(f'{self.name} are currently working as a ...')

    def __repr__(self) -> str:
        return f'Employee {self.name}'


class Chef(Employee):
    def __init__(self, name):
        super().__init__(name, 50000)

    def work(self):
        print(f"{self.name} is a Chef at a restaurant")


class Servant(Employee):
    def __init__(self, name):
        super().__init__(name, 25000)

    def work(self):
        print(f"{self.name} is a Servant at the restaurant")


class FoodRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(f'{self.name} Is delivering and cleaning the food')


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, servant):
        print(f'{self.name} takes orders from {str(servant)}')

    def pay(self, servant):
        print(f'{self.name} pays for item to {str(servant)}')


class Oven:
    def cook(self):
        print('Cooking something...')


class FoodShop:
    def __init__(self) -> None:
        self.servant = Servant('Michael')
        self.robot_chef = FoodRobot('Wall-E')
        self.oven = Oven(kwa)

    def order(self, name):
        # behöver en kund för att beställa
        customer = Customer(name)
        customer.order(self.servant)
        self.robot_chef.work()
        self.oven.cook()
        customer.pay(self.servant)


building = FoodShop()
building.order('Maxwell')
print('Done')
building.order('Kiara')
