from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self) -> None:
        self.legs = self.no_of_legs()

    @abstractmethod
    def no_of_legs(self):
        return

    def move(self):
        print(f'Moving with {self.legs} legs')


class Human(Animal):
    def no_of_legs(self):
        return 2


gustav = Human()
gustav.move()
