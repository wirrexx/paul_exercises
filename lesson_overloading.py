from functools import singledispatchmethod


class Point:

    @singledispatchmethod
    def set(self, arg):  # föräldrar metoden
        raise NotImplementedError()

    @set.register  # barn metoden som blir kallade, samma namn med float
    def _(self, lat: int, lng: int):
        self.lat = lat
        self.lng = lng

    @set.register  # barn metoden som blir kallade, samma namn med index
    def _(self, coords: list):
        self.lat = coords[0]
        self.lng = coords[1]


point1 = Point()
point2 = Point()

point1.set(2, 3)  # method overloading in action
point2.set([5, 4])  # method overloading in action

print(f"Point: ({point1.lat}, {point1.lng})")
print(f"Point: ({point2.lat}, {point2.lng})")
