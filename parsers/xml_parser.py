from abstracted.abstracted_parser import AbstractedBaseParser

import xmltodict
import json

class XMLParser(AbstractedBaseParser):
    def parse_string(self, input_data):
        output = xmltodict.parse(input_data)
        
        return json.dumps(output, indent=4)
        