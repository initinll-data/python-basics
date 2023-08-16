from typing import Protocol

# interface


class Animal(Protocol):
    # interface method
    def breathe(self) -> None:
        pass


class Mammal():
    def __init__(self) -> None:
        self.weight = 2

    def walk(self):
        print("walk")

    def eat(self):
        # method overriding
        print("eating")

    def breathe(self) -> None:
        print("Mammal is breathing")


class Fish():
    def swim(self):
        print("swim")

    def breathe(self) -> None:
        print("Fish is breathing")


# polymorphism using protocols
def get_animal(animal: Animal) -> None:
    animal.breathe()


mammal = Mammal()
fish = Fish()
get_animal(mammal)
get_animal(fish)
