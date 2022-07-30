from abc import ABC, abstractmethod


class Duck(ABC):
    def __init__(self):
        self.fly_behaviour = None
        self.quack_behaviour = None

    @staticmethod
    def swim():
        return "all ducks can swim"

    @abstractmethod
    def display(self):
        raise NotImplemented

    def perform_quack(self):
        return self.quack_behaviour.quack()

    def perform_fly(self):
        return self.fly_behaviour.fly()

    def set_fly_behaviour(self, fly_behaviour):
        self.fly_behaviour = fly_behaviour

    def set_quack_behaviour(self, quack_behaviour):
        self.quack_behaviour = quack_behaviour


class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplemented


class QuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        raise NotImplemented


class FlyWithWings(FlyBehaviour):
    def fly(self):
        return "i am flying with wings"


class FlyRocket(FlyBehaviour):
    def fly(self):
        return "flying with rocket"


class Quack(QuackBehaviour):
    def quack(self):
        return "Quack Quack Quack"


class MallardDuck(Duck):
    def display(self):
        return "hi, i am MAllard"

    def __init__(self):
        super().__init__()
        self.quack_behaviour = Quack()
        self.fly_behaviour = FlyWithWings()


ml = MallardDuck()
print(ml.perform_fly())
ml.perform_quack()
ml.set_fly_behaviour(FlyRocket())
print(ml.perform_fly(), ml.display())
