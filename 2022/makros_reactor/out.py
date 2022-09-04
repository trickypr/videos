# Macro imported: enum


class Animals:
    def __assign_enum_types__(Animals, cat, dog, other):
        Animals.Cat = cat
        Animals.Dog = dog
        Animals.Other = other

    def __eq__(self, other):
        return isinstance(self, other)


class Cat(Animals):
    def __str__(self):
        return "Cat"


class Dog(Animals):
    def __str__(self):
        return "Dog"


class Other(Animals):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Other(name: {self.name})"


Animals.__assign_enum_types__(Animals, Cat, Dog, Other)


del Cat
del Dog
del Other


cat = Animals.Cat
lion = Animals.Other("Lion")
assert cat != lion
assert cat == Animals.Cat
assert lion == Animals.Other
print(lion.name)
