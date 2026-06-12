from pathlib import Path

from .exceptions import MethodNotFoundException

import os
import json

class OutputHandler:
    def get_io_mode(self, output_path):
        if os.path.exists(output_path):
            return "w"
                
        else:
            return "x"
        
    def proccess_output(self, factory, data, method):
        def method_not_found(data):
            raise MethodNotFoundException
        
        parser = factory.create_parser()
        
        return getattr(parser, method, method_not_found)(data)
        
        
    def save_output(self, output, output_file, print_output):
        if print_output:
            print(output)
        
        output_path = Path(output_file).resolve()   

        mode = self.get_io_mode(output_path)
            
        with open(output_path, mode)as f:
            if output_path.suffix == ".json":
                json.dump(output, f, indent=4)

            else:            
                f.write(output)

