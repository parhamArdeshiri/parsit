from io import StringIO
from abstracted.abstracted_parser import AbstractedBaseParser

import yaml
import json

class YMLParser(AbstractedBaseParser):
    def to_json(self, input_data):
        data = StringIO(input_data)
        output = yaml.load(data, Loader=yaml.SafeLoader)
        
        return output
    
    def from_json(self, input_data):
        output = yaml.dump(input_data, default_flow_style=False) 

        return output
    