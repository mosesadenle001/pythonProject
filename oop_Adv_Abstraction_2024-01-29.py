from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, value, currency):
        self.value = value
        self.currency = currency
        self.get_value = 500
        self.currency = '$'
        self.convert_to_currency = '$'

    @abstractmethod
    def get_value(self):
        if self.value:
            self.value += 500
    @abstractmethod
    def get_currency(self):
   @abstractmethod
    def convert_to_currency
