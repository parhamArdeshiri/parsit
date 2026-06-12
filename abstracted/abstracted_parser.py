from abc import ABC, abstractmethod
from pathlib import Path

class AbstractedBaseParser(ABC):
    @abstractmethod
    def to_json(self, input_data):
        pass
    
    @abstractmethod
    def from_json(self, input_data):
        pass
    