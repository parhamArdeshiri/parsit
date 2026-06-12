from settings import factories
from pathlib import Path

import sys

class InputHandler:
    def get_factory(self, input_data, input_type):
          
        if input_type:
            return factories.get(input_type)
            
        elif input_data:
            input_path = Path(input_data)
            
            return factories.get(
                input_path.suffix
            )
            
        else:
            raise ValueError(
                "You neither must implement input_type and data using stdin or give an input data as the default arg\n"
                "If you implemet all of these args the priority is with the input_type and stdin value"
            )
                
    def parse_data(self, input_data, input_type):
        stdin = None

        if not sys.stdin.isatty():
            stdin = sys.stdin.read()    
                
        if stdin and input_type:
            return (stdin, input_type)
            
        elif input_data:
            input_path = Path(input_data).absolute()
            
            with open(input_path, "r") as f:
                return f.read() 
        
        else:
            raise ValueError(
                "You neither must implement input_type and data using stdin or give an input data as the default arg\n"
                "If you implemet all of these args the priority is with the input_type and stdin value"
            )
                
        