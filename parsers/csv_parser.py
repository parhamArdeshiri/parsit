from io import StringIO
from abstracted.abstracted_parser import AbstractedBaseParser

import csv
import json

class CSVParser(AbstractedBaseParser):
    def parse_string(self, input_data):
        csv_data = StringIO(input_data)
        output = list(csv.DictReader(csv_data))
        
        return json.dumps(output, indent=4)
        