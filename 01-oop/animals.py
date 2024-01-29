from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def sound(self):
        pass

    def test(self):
        print("Just a test")

class Dog(Animal):
    def sound(self):
        print("Wooof")

class Cat(Animal):
    def sound(self):
        print("Mieow")


c = Cat()
c.sound()