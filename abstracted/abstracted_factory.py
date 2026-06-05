from abc import ABC, abstractmethod

from abstracted_parser import AbstractedBaseParser

class AbstractedBaseFactory(ABC):
    @abstractmethod
    def create_parser(self) -> AbstractedBaseParser:
        pass
    
    def perform_parsing(self, data):
        parser = self.create_parser()
        return parser.parse(data)
    