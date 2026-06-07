from settings import factories
from pathlib import Path

import os
import sys

def to_json(input_data=None, output="output.json", input_type=None, print_output=None):
    factory = None
        
    if input_type:
        factory = factories.get(input_type)
        data = sys.stdin.read() if not input_data else input_data
        
    else:
        factory = factories.get(
            input_data.split(".")[-1]
        )
        data = Path(input_data)
        
        
    output_data = factory.perform_parsing(data, output)
    
    if print_output:
        print(output_data)
    
    output_path = Path(output).resolve()   

    if os.path.exists(output_path):
        mode = "w"
            
    else:
        mode = "x"
        
    with open(output_path, mode)as f:
        f.write(output_data)