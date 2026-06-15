from abstracted.abstracted_parser import AbstractedBaseParser

import toml
import json

class TOMLParser(AbstractedBaseParser):
    def to_json(self, input_data):
        output = toml.loads(input_data)
        
        return output
        
    def from_json(self, input_data):        
        output = toml.dumps(input_data)
        
        return output
    