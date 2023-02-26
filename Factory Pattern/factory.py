from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        return "WOUOUWOU"

class Cat(Animal):

    def speak(self):
        return "meow"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        if animal_type == "cat":
            return Cat()

        else:
            raise ValueError("Invalid animal type")

factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")


