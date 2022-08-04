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
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None

    @abstractmethod
    def update(self):
        raise "not implemented"


class DisplayElement(ABC):

    @abstractmethod
    def display(self):
        raise "not implemented"





