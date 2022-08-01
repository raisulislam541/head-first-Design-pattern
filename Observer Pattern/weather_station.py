from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def register_observer(self):
        raise "not implemented"

    @abstractmethod
    def remove_observer(self):
        raise "not implemented"

    @abstractmethod
    def notify_observers(self):
        raise "not implemented"

class Observer(ABC):




