from io import StringIO
from abstracted.abstracted_parser import AbstractedBaseParser

import yaml
import json

class YMLParser(AbstractedBaseParser):
    def parse_string(self, input_data):
        data = StringIO(input_data)
        output = yaml.load(data, Loader=yaml.SafeLoader)
        
        return json.dumps(output, indent=4)
