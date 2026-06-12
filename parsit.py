import fire
import os

from pathlib import Path

from cli.input_handler import InputHandler
from cli.output_handler import OutputHandler

class CLI:
    def __init__(self):
        self.__input_handler = InputHandler()
        self.__output_handler = OutputHandler()
    
    def convert(self,
                 input_data: str = "", 
                 input_type: str = "",
                 output_file: str = "", 
                 print_output: bool = False):
        
        factory = self.__input_handler.get_factory(
            input_data,
            input_type
        )
        
        data = self.__input_handler.parse_data(
            input_data,
            input_type            
        )
        
        output = self.__output_handler.proccess_output(
            factory,
            data,
            method="to_json"
        )
        
        output_path = Path(output_file)
        
        if output_path.suffix:
            output_type = output_path.suffix
            
            if output_type != "json":
                output_factory = self.__input_handler.get_factory(
                    input_data=None,
                    input_type=output_type
                )
                
                output = self.__output_handler.proccess_output(
                    output_factory,
                    output,
                    method="from_json"
                )
                
            self.__output_handler.save_output(
                output,
                output_path,
                print_output
            )
            
        else:
            path = os.path.join(output_path, "output.json")
            
            self.__output_handler.save_output(
                output,
                path,
                print_output
            )
                

if __name__ == "__main__":
    fire.Fire(CLI)
    