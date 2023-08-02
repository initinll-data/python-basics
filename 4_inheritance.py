from abc import ABC, abstractmethod


# abstract base class
class Animal(ABC):
    def __init__(self) -> None:
        self.age: int = 1
        self.__alive: bool = True

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, value: bool):
        self.__alive = value

    def eat(self):
        print("eat")

    # abstract method
    @abstractmethod
    def breathe(self) -> None:
        pass


class Mammal(Animal):
    def __init__(self) -> None:
        super().__init__()
        self.weight = 2

    def walk(self):
        print("walk")

    def eat(self):
        # method overriding
        print("eating")
        # base class method
        super().eat()

    def breathe(self) -> None:
        print("Mammal is breathing")


class Fish(Animal):
    def swim(self):
        print("swim")

    def breathe(self) -> None:
        print("Fish is breathing")


# polymorphism
def get_animal(animal: Animal) -> None:
    animal.breathe()


mammal = Mammal()
mammal.eat()
mammal.walk()
mammal.breathe()
print(mammal.age)
print(mammal.weight)
print(mammal.alive)
get_animal(mammal)
