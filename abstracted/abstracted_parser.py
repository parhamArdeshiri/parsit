from abc import ABC, abstractmethod
from pathlib import Path

class AbstractedBaseParser(ABC):
    @abstractmethod
    def parse_string(self, input_data):
        pass
    
    def parse(self, input_data, output):
        if isinstance(input_data, str):
            output_data = self.parse_string(input_data)
        
        elif isinstance(input_data, Path):            
            with open(input_data, 'r') as file:
                output_data = self.parse_string(file.read())
            
        else:
            raise ValueError("Unsupported data type for parsing")
        
        with open(output, "w") as f:
            f.write(output_data)
            
        return output_data
        