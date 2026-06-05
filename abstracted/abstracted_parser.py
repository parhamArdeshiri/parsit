from abc import ABC, abstractmethod
from pathlib import Path

class AbstractedBaseParser(ABC):
    @abstractmethod
    def parse_string(self, data):
        pass
    
    def parse(self, data):
        if isinstance(data, str):
            return self.parse_string(data)
        
        elif isinstance(data, Path):
            with open(data, 'r') as file:
                return self.parse_string(file.read())
            
        else:
            raise ValueError("Unsupported data type for parsing")