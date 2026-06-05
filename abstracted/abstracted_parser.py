from abc import ABC, abstractmethod
from pathlib import Path

class AbstractedBaseParser(ABC):
    @abstractmethod
    def parse_string(self, data):
        pass
    
    def parse(self, input_data, output_file):
        if isinstance(input_data, str):
            output = self.parse_string(input_data)
        
        elif isinstance(input_data, Path):
            with open(input_data, 'r') as file:
                output = self.parse_string(file.read())
            
        else:
            raise ValueError("Unsupported data type for parsing")
        
        with open(output_file, "w") as f:
            f.write(output)
            
        return output
        