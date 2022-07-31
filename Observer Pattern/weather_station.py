from abc import ABC, abstractmethod


class Subject(ABC):
    def register_observer(self):
        raise "not implemented"

    def remove_observer(self):


